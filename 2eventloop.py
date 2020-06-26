import socket
from select import select


to_monitor = []

server_socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socker.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socker.bind(('localhost', 5000))
server_socker.listen()


def accept_connection(server_socker):
    client_socket, addr = server_socker.accept()
    print('Connection from', addr)
    to_monitor.append(client_socket)



def send_message(client_socket):
    
    request = client_socket.recv(4096)

    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()



def event_loop():
    while True:
        
        ready_to_read, _, _ = select(to_monitor, [], [])

        for sock in ready_to_read:
            if sock is server_socker:
                accept_connection(sock)
            else:
                send_message(sock)




if __name__ == "__main__":
    to_monitor.append(server_socker)
    event_loop()