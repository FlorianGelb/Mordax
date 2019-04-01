import os
import Client


class Console(Client.Client):
    def __init__(self):
        self.client = Client.Client()
        self.set_version(1.0)
        self.start()

    def start(self):
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
            print("help             shows help          ")
            print("                                      ")
            os.system("pause")
            self.start()
        elif x == "connect":
            self.client.connect(0)
        if x == "check":
            self.check_version()
        elif x == "update":
            self.download_version("console.py")
        if x == "scan":
            self.client.scan()

        else:
            print("command not found")
            self.start()


if __name__ == "__main__":
    Con = Console()

