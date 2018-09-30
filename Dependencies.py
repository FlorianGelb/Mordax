import os
import sys

class Dependencies:

        if sys.version_info[0] > 2 and sys.version_info[1] < 7:
            print("Python 2.7 or higher is required.")

    def checkLibraries(self):
        try:
            import Crypto
            import requests
            import tqdm
        except Exception as e:
            missingModule = str(e).split("No module named ")
            print ("{} is required ".format(missingModule[1]))

            inp = raw_input("Do you want to install {} (y/n) \n".format(missingModule[1]))
            if inp == "y":
                self.installLibraries(missingModule[1])
            elif inp == "n":
                return 0
            else:
                print("{} is no aviable option".format(inp))

    def installLibraries(self, missingLibraries):
        try:
            os.system("pip install {}".format(missingLibraries))
        except Exception as e:
            print(e)


