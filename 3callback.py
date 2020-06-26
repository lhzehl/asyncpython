import socket
import selectors
# >>> selectors.DefaultSelector()
# <selectors.SelectSelector object at 0x000002C26B790AF0>

selector = selectors.DefaultSelector()

def server():
    server_socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socker.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socker.bind(('localhost', 5000))
    server_socker.listen()

    selector.register(fileobj=server_socker, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socker):
    client_socket, addr = server_socker.accept()
    print('Connection from', addr)
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)




def send_message(client_socket):
    
    request = client_socket.recv(4096)

    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()




def event_loop():
    while True:
        
        events = selector.select() # (key, events)

        # SelectorKey => [fileobj, events, data]

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)
        



if __name__ == "__main__":
    server()
    event_loop()