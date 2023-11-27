export PYTHONPATH=./proto:$PYTHONPATH

run_cli_pares: server_pb2.py centralServer_pb2.py
	python3 cln_par.py $(arg)

run_serv_pares_1: server_pb2.py centralServer_pb2.py
	python3 svc_par.py $(arg)

run_serv_pares_2: server_pb2.py centralServer_pb2.py
	python3 svc_par.py $(arg) --servent

run_serv_central: server_pb2.py centralServer_pb2.py
	python3 svc_cen.py $(arg)

run_cli_central: server_pb2.py centralServer_pb2.py
	python3 cln_cen.py $(arg)

server_pb2.py: server.proto
	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. server.proto

centralServer_pb2.py: centralServer.proto
	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. centralServer.proto

clean:
	rm -f *_pb2*.*
	rm -rf __pycache__