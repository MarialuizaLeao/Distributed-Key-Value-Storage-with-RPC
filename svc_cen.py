from concurrent import futures
import sys
import grpc
import socket
import threading
from proto import centralServer_pb2 as centralMessages
from proto import centralServer_pb2_grpc as centralServices

# its a subclass of the centralServerServicer class, which is the class generated by the compiler
class centralServer(centralServices.centralServerServicer):
    def __init__(self, stop_event):
        
        super(centralServer, self).__init__()
        
        self.serversDict = dict() # dictionary to store the pairs (key, serverID)
        self._stop_event = stop_event # stop event to terminate the server only after isends the response to the client
        
    def register(self, request, context) -> int:
        
        """
            
            ● register: receives as parameter the service identifier string that identifies a
            -----------  key/value pair storage server and the list of keys (integers) stored in it, stores
                         each key in its directory, associating them with the received service identifier,
                         and returns the number of keys that were processed;

        """
        
        serverID = request.serverID # server host:port
        keyList = [key for key in request.keyList] # list of keys that the server has
        for key in keyList: 
            self.serversDict[key] = serverID
        return centralMessages.registerResponse(amountOfRegisteredKeys = len(keyList))
        
    def map(self, request, context) -> int:
        
        """
            
            ● map: receives as parameter a positive integer ch, consults its directory of keys
            -----  by server and returns the service identifier string associated with the server that
                   contains a pair with that key, or an empty string if it does not find such a server;
        
        """
        
        key = request.key
        if key in self.serversDict:
            return centralMessages.mapResponse(serverID = self.serversDict[key])
        else:
            return centralMessages.mapResponse(serverID = "")
        
    def terminate(self, request, context):
        
        """
            
            ● terminate: terminates the operation of the central server only, returns the number
            -----------  of keys that were registered and ends.
        
        """
        self._stop_event.set() # set the stop event to terminate the server
        return centralMessages.terminateResponse(amountOfRegisteredKeys = len(self.serversDict))
        
def run():
    # create the stop event, this is used to terminate the server after the client sends the terminate command
    stop_event = threading.Event()
    
    # create the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # add the centralServerServicer to the server
    centralServices.add_centralServerServicer_to_server(centralServer(stop_event), server)
    
    # set to default host
    host = "0.0.0.0"
    
    # get the port from the command line
    port = sys.argv[1]
    
    # add the insecure port to the server
    server.add_insecure_port(f"{host}:{port}")
    
    # start the server
    server.start()
    
    # wait for the stop event
    stop_event.wait()
    
    # wait 1 second(so the message can be send to the client before it terminates) and stop the server
    server.stop(1)
    
if __name__ == "__main__":
    run()