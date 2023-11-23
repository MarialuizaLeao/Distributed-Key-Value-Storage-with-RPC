from concurrent import futures
import sys
import grpc
import socket
import threading
from proto import centralServer_pb2 as messages
from proto import centralServer_pb2_grpc as services

class centralServer(services.centralServerServicer):
    def __init__(self, stop_event):
        
        super(centralServer, self).__init__()
        
        self.serversDict = dict()
        self._stop_event = stop_event
        
    def register(self, request, context) -> int:
        serverID = request.serverID
        keyList = [key for key in request.keyList]
        for key in keyList: 
            self.serversDict[key] = serverID
        return messages.registerResponse(amountOfRegisteredKeys = len(keyList))
        
    def map(self, request, context) -> int:
        key = request.key
        if key in self.serversDict:
            return messages.mapResponse(serverID = self.serversDict[key])
        else:
            return messages.mapResponse(serverID = "")
        
    def terminate(self, request, context):
        self._stop_event.set()
        return messages.terminateResponse(amountOfRegisteredKeys = len(self.serversDict))
        
def run():
    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services.add_centralServerServicer_to_server(centralServer(stop_event), server)
    host = socket.getfqdn()
    port = sys.argv[1]
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    stop_event.wait()
    server.stop(1)
    
if __name__ == "__main__":
    run()