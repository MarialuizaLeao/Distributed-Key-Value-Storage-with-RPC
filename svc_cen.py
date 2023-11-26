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
        
        """

            ● registro: recebe como parâmetro o string identificador de serviço que identifica
            um servidor de armazenamento de pares chave/valor e a lista de chaves
            (inteiros) nele armazenadas, armazena cada chave em seu diretório,
            associando-as ao identificador de serviço recebido, e retorna o número de
            chaves que foram processadas;

        """
        
        serverID = request.serverID
        keyList = [key for key in request.keyList]
        for key in keyList: 
            self.serversDict[key] = serverID
        return messages.registerResponse(amountOfRegisteredKeys = len(keyList))
        
    def map(self, request, context) -> int:
        
        """
            ● mapeamento: recebe como parâmetro um inteiro positivo ch, consulta o seu
            diretório de chaves por servidor e retorna o string identificador de serviço
            associado ao servidor que contém um par com aquela chave, ou um string vazio,
            caso não encontre tal servidor;
        
        """
        
        key = request.key
        if key in self.serversDict:
            return messages.mapResponse(serverID = self.serversDict[key])
        else:
            return messages.mapResponse(serverID = "")
        
    def terminate(self, request, context):
        
        """
        
            ● término: encerra a operação do servidor centralizador apenas, retorna o número
            de chaves que estavam registradas e termina.
        
        """
        self._stop_event.set()
        return messages.terminateResponse(amountOfRegisteredKeys = len(self.serversDict))
        
def run():
    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services.add_centralServerServicer_to_server(centralServer(stop_event), server)
    host = "0.0.0.0"
    port = sys.argv[1]
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    stop_event.wait()
    server.stop(1)
    
if __name__ == "__main__":
    run()