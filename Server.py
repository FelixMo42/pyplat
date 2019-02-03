import socket
import select
import sys
import threading
import queue
import json

HOST = "localhost"#socket.gethostname()
PORT = 10000

IDs = 0

class Client(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)

        self.connection = connection
        self.address = address

        self.x = 0
        self.y = 0
        self.velX = 0
        self.velY = 0

    def run(self):
        global IDs
        msg = (str(IDs) + "\n").encode('utf-8')
        print(msg)
        self.connection.sendall(msg)
        IDs += 1

        while True:
            data = self.recv()
            if data:
                print(data)

    def recv(self):
        data = ""
        while True:
            data += self.connection.recv(4096).decode()
            if "\n" in data:
                break
        return str(data)[:-1]



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind((HOST, PORT))
server.listen(5)

print("hosting on {HOST}:{PORT}".format(HOST=HOST, PORT=PORT))

inputs = [server]
outputs = []
clients = []
message_queues = {}

ids = 0

testData = json.dumps({
    "velX": 0, "velY": 0,
    "x": 0, "y": 0,
    "id":"-1"
}).encode("utf-8") + b"\n"

def deregister(connection):
    inputs.remove(s)
    clients.remove(s)
    if s in outputs:
        outputs.remove(s)
    s.close()
    del message_queues[s]

try:
    while True:
        readable, writable, exceptional = select.select(
            inputs,
            outputs,
            inputs
        )

        for s in readable:
            if s is server:
                connection, addres = s.accept()
                connection.sendall((str(ids) + "\n").encode('utf-8'))
                connection.setblocking(0)
                inputs.append(connection)
                clients.append(connection)
                message_queues[connection] = queue.Queue()
                print("new client")
            else:
                try:
                    data = s.recv(1024)
                    if data:
                        for client in clients:
                            if client is not s:
                                message_queues[client].put(data)
                                if client not in outputs:
                                    outputs.append(s)
                        message_queues[s].put(testData)
                        outputs.append(s)
                    else:
                        if s in outputs:
                            outputs.remove(s)
                        inputs.remove(s)
                        s.close()
                        del message_queues[s]
                except ConnectionResetError as exception:
                    deregister(s)

        for s in writable:
            try:
                next_msg = message_queues[s].get_nowait()
            except queue.Empty:
                outputs.remove(s)
            else:
                s.send(next_msg)

        for s in exceptional:
            deregister(s)
finally:
    server.close()
    print("server closed")

'''
try:
    while True:
        select.
        (connection, address) = server.accept()
        ct = Client(
            connection=connection,
            address=address
        )
        
        ct.start()
        clients.append(ct)
except KeyboardInterrupt as interrupt:
    print("")
finally:
    server.close()
    print("server closed")
'''