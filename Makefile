
.PHONY: clean run_cli_pares run_serv_pares_1 run_serv_pares_2 run_serv_central run_cli_central

clean:
    # Remove all intermediate files
    rm -rf intermediate_files

run_cli_pares:
    # Run the client program of the first part
    ./client_pares

run_serv_pares_1:
    # Run the peer server program with the behavior of the first part
    ./server_pares_1

run_serv_pares_2:
    # Run the peer server program with the behavior of the second part
    ./server_pares_2

run_serv_central:
    # Run the server program of the second part
    ./server_central

run_cli_central:
    # Run the client program of the second part
    ./client_central
