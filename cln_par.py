from concurrent import futures
import sys
import grpc
import socket
import logging
import server_pb2
import server_pb2_grpc

def run():
    # open a channel to the server
    channel = grpc.insecure_channel(f"{sys.argv[1]}")
    
    # create the stub, which will be the object with references to the
    # remote procedures (code generated by the compiler)
    stub = server_pb2_grpc.serverStub(channel)
    
    while True:
        # read the input from the client
        try:
            clientInput  = input().split(",", maxsplit = 2)
        except EOFError:
            break
        command = clientInput[0]
        
        if command == "I":
            
            """
            
                ● I,ch,decision string - insert the key ch and the string value in the server,
                ------------------------  writing the return value to the output (0 if successful, -1 if the key already
                                          exists);

            """

            key = clientInput[1] # ch
            value = clientInput[2] # decision string
            response = stub.insert(server_pb2.insertRequest(key = int(key), value = str(value))) # request to the server
            print(str(response.success))
        
        elif command == "C":
        
            """
            
                ● C,ch - consult the value associated with the key ch, writing the return value
                -------- to the output (the empty string if the key does not exist);

            """
            key = clientInput[1] # ch
            response = stub.consult(server_pb2.consultRequest(key = int(key))) # request to the server
            print(str(response.value))
        
        elif command == "A":
            
            """
            
                ● A,service ID string - activate the service, writing the return value to the
                ----------------------- output (the number of keys that were activated, or 0 if the service is not
                                        active);

            """
            service = clientInput[1] # service ID string
            response = stub.activate(server_pb2.activateRequest(centralServerID = str(service))) # request to the server
            print(str(response.amountOfActivatedKeys))
        
        elif command == "T":
            
            """
            
                ● T - triggers the server termination operation, writes the return value to the output
                ----  and ends the client.

            """
            
            response = stub.terminate(server_pb2.Empty()) # request to the server
            print(str(response.key))
            break
        
    # at the end the client can close the channel to the server.
    channel.close()
    
if __name__ == '__main__':
    run()