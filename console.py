import os
import Client
import string

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
        elif x == "payload":
            client.create_payload()


        if x.startswith("scan"):
            if x[4:] == " -log":
                client.scan("log")
            if x[4:] == " -aa"
                client.scan("aa")

        else:
            print("command not found")
            self.start()



Con = Console()
Con.start()