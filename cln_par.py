from concurrent import futures
import sys
import grpc
import socket
import server_pb2 as messages
import server_pb2_grpc as services

def run():
    # Primeiro, é preciso abrir um canal para o servidor
    channel = grpc.insecure_channel(f"{sys.argv[1]}")
    # E criar o stub, que vai ser o objeto com referências para os
    # procedimentos remotos (código gerado pelo compilador)
    stub = services.serverStub(channel)
    
    while True:
        clientInput  = input().split(",")
        command = clientInput[0]
        if command == "I":
            key = clientInput[1]
            value = clientInput[2]
            response = stub.insert(messages.insertRequest(key = int(key), value = str(value)))
            print(str(response.success))
        elif command == "C":
            key = clientInput[1]
            response = stub.consult(messages.consultRequest(key = int(key)))
            print(str(response.value))
        elif command == "A":
            service = clientInput[1]
            response = stub.activate(messages.activateRequest(centralServerID = str(service)))
            print(str(response.amountOfActivatedKeys))
        elif command == "T":
            response = stub.terminate(messages.Empty())
            print(str(response.key))
            break
    # Ao final o cliente pode fechar o canal para o servidor.
    channel.close()
    
if __name__ == '__main__':
    run()