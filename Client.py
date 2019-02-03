import socket
import threading
import sys

class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = ('localhost', 10000)
        print('connecting to {} port {}'.format(*server_address))
        self.connection.connect(server_address)
        print('connected to {} port {}'.format(*server_address))

    def run(self):
        try:
            # Send data
            message = b'This is the message.  It will be repeated.'
            print('sending {!r}'.format(message))
            self.connection.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.connection.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))

        finally:
            print('closing socket')
            self.connection.close()