from concurrent import futures
import sys
import grpc
import socket
from proto import centralServer_pb2 as centralMessages
from proto import centralServer_pb2_grpc as centralServices
from proto import server_pb2 as messages
from proto import server_pb2_grpc as services

def run():
    # Primeiro, é preciso abrir um canal para o servidor
    channel = grpc.insecure_channel(f"{sys.argv[1]}")
    # E criar o stub, que vai ser o objeto com referências para os
    # procedimentos remotos (código gerado pelo compilador)
    stub = centralServices.centralServerStub(channel)
    
    while True:
        clientInput  = input().split(",")
        command = clientInput[0]
        if command == "C":
            key = clientInput[1]
            response = stub.map(centralMessages.mapRequest(key = int(key)))
            serverID = response.serverID
            if serverID != "":
                print(f"{str(serverID)}:")
                channelServer = grpc.insecure_channel(serverID)
                stubServer = services.serverStub(channelServer)
                response = stubServer.consult(messages.consultRequest(key = int(key)))
                print(f"{str(response.value)}")
        elif command == "T":
            response = stub.terminate(centralMessages.Empty())
            print(str(response.amountOfRegisteredKeys))
            break
    # Ao final o cliente pode fechar o canal para o servidor.
    channel.close()
    
if __name__ == '__main__':
    run()