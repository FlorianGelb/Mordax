import os
import threading
import Client
from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)
import multiprocessing


def start():
    os.system("cls")
    print("                         .___              ")
    print("  _____   ___________  __| _/____  ___  ___")
    print(" /     \ /  _ \_  __ \/ __ |\__  \ \  \/  /")
    print("|  Y Y  (  <_> )  | \/ /_/ | / __ \_>    < ")
    print("|__|_|  /\____/|__|  \____ |(____  /__/\_ |")
    print("      \/                  \/     \/      \/")
    print("                                           ")
    print("                                           ")
    print("                                           ")
    print("                                           ")
    print("                                           ")


    x = raw_input("<command>: ")
    x = str(x)


    if x == "help":
        print("connect          connect to another pc")
        print("                                      ")
        print("scan             scan infected IPs    ")
        print("                                      ")
        print("help             showes help          ")
        print("                                      ")
        os.system("pause")
        start()

    elif x == "connect":
        Client.connect(0)

    elif x == "scan":
       Client.scan("none")
    elif x == "scan -log":
        Client.scan("log")


    else:
        print("command not found")
        start()



start()