import os
import socket
import sys
import time
import threading
from multiprocessing.pool import ThreadPool


def connect(host):
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

    text = "<command:>"
    SIZE = 2048
    while True:
        cmd = raw_input(text)
        if cmd == "close":
            s.send("close")
            s.close()
            exit()
        s.send(cmd)
        data = s.recv(2048)
        data = data.split(";")

        if data[0] == "SIZE":
            data[1] = int(data[1])
            data2 = s.recv(data[1])
            data2 = data2.split(";")
            print (data2[0])
            text = data2[1] + ">"
        else:
            print data[0]
            text = data[1] + ">"





def scan(args):
   start = raw_input("Start IP: ")
   stop = raw_input("Stop IP: ")


   ip1 = start.split(".")
   ip2 = stop.split(".")

   range1 = ip1[0] + "." + ip1[1] + "." + ip1[2] + "."

   tip = int(ip1[3])
   t1ip = int(ip1[3]) + 1
   t2ip = int(ip1[3]) + 2
   t3ip = int(ip1[3]) + 3
   t4ip = int(ip1[3]) + 4
   t5ip = int(ip1[3]) + 5
   t6ip = int(ip1[3]) + 6
   t7ip = int(ip1[3]) + 7

   t1 = threading.Thread(target=sscan, args=(tip,ip2[3],"9",args,"0",range1))
   t2 = threading.Thread(target=sscan, args=(t1ip,ip2[3],"9",args,"1",range1))
   t3 = threading.Thread(target=sscan, args=(t2ip,ip2[3],"9",args,"2",range1))
   t4 = threading.Thread(target=sscan, args=(t3ip,ip2[3],"9",args,"3",range1))
   t5 = threading.Thread(target=sscan, args=(t4ip,ip2[3], "9", args,"4",range1))
   t6 = threading.Thread(target=sscan, args=(t5ip,ip2[3], "9", args,"5",range1))
   t7 = threading.Thread(target=sscan, args=(t6ip,ip2[3], "9", args,"6",range1))
   t8 = threading.Thread(target=sscan, args=(t7ip,ip2[3], "9", args,"7",range1))

   t1.start()
   t2.start()
   t3.start()
   t4.start()
   t5.start()
   t6.start()
   t7.start()
   t8.start()


def sscan(strange,srange, step,args,thread,iprange):

    try:

        for x in range(strange,int(srange),int(step)):
            if x < 10:
                x = str(x)
                x = "0" + x
            elif x >= 10:
                x = str(x)
            ip = iprange + x
            if args == "none":
                print("scanning")
            if args == "log":
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

