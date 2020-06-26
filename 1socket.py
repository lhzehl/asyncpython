import socket
#  accept telnet win10 pkgmgr /iu:”TelnetClient” 
# domain:port

server_socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socker.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socker.bind(('localhost', 5000))
server_socker.listen()



while True:
    print('Before accept')
    client_socket, addr = server_socker.accept()
    print('Connection from', addr)

    while True:

        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)

    print('Outside inner while loop')
    client_socket.close()
