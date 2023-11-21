from concurrent import futures
import sys
import grpc
import socket
import threading
import server_pb2 as messages
import server_pb2_grpc as services
import centralServer_pb2 as centralMessages
import centralServer_pb2_grpc as centralServices

# subclasse de serverServicer que implementa os métodos do servidor
class Server(services.serverServicer):
    def __init__(self, stop_event, flag = False):
        super(Server, self).__init__()
        self.flag = flag
        self.pairs = dict()
        self.ID = f"{socket.getfqdn()}:{sys.argv[1]}"
        self._stop_event = stop_event
        
    def insert(self, request, context) -> int:
        key = request.key
        value = request.value
        if key in self.pairs:
            return messages.insertResponse(success = -1)
        else:
            self.pairs[key] = value
            return messages.insertResponse(success = 0)
    
    def consult(self, request, context) -> str:
        key = int(request.key)
        if key in self.pairs:
            return messages.consultResponse(value = self.pairs[key])
        else:
            return messages.consultResponse(value = "")
        
    def activate(self, request, context) -> int:
        """ 
            returns 0 if flag is not true
            if flag is true, the server will connect to the central server and make a request to activate the service
            it will send to the central server its ID(host:port) and a list with the key in the pairs dictionary
            returns the amount of keys that were activated
        """
        if not self.flag:
            return messages.activateResponse(amountOfActivatedKeys = 0)
        else:
            channel = grpc.insecure_channel(request.centralServerID)
            stub = centralServices.centralServerStub(channel)
            response = stub.register(centralMessages.registerRequest(serverID = str(self.ID), keyList = list(self.pairs.keys())))
            return messages.activateResponse(amountOfActivatedKeys = int(response.amountOfRegisteredKeys))
    
    def terminate(self, request, context):
        self._stop_event.set()
        return messages.terminateResponse(key = 0)
    
def run():
    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    if len(sys.argv) == 3:
        services.add_serverServicer_to_server(Server(stop_event, flag = True), server)
    else:
        services.add_serverServicer_to_server(Server(stop_event), server)
    host = socket.getfqdn()
    port = sys.argv[1]
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    stop_event.wait()
    server.stop(1)
    
if __name__ == "__main__":
    run()
        