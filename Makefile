run_cli_pares: server_pb2.py centralServer_pb2.py
	python3 cln_par.py $(arg)

run_serv_pares_1: server_pb2.py centralServer_pb2.py
	python3 svc_par.py $(arg)

run_serv_pares_2: server_pb2.py centralServer_pb2.py
	python3 svc_par.py $(arg) --servent

run_serv_central: server_pb2.py centralServer_pb2.py
	pytho3 svc_cen.py $(arg)

run_cli_central: server_pb2.py centralServer_pb2.py
	python3 cln_cen.py $(arg)

server_pb2.py: proto/server.proto
	python3 -m grpc_tools.protoc --proto_path=./proto --python_out=./proto --grpc_python_out=./proto server.proto

centralServer_pb2.py: proto/centralServer.proto
	python3 -m grpc_tools.protoc --proto_path=./proto --python_out=./proto --grpc_python_out=./proto centralServer.proto

clean:
	rm -f proto/*_pb2*.* 
	rm -rf __pycache__