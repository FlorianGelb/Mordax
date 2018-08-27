import os
import sys
import time

class Compile:

    def check(self,programm):

        version = sys.version_info
        version1 = str(version[0])
        version2 = str(version[1])

        try:
            import py2exe
        except Exception:
            print ("PY2EXE is required.")

        if version1 == "2":
            self.programm = programm
        elif version1 == "3":
            if version2 > "4":
                print("PY2EXE isn't supporting Pyhton " + version1 + "." + version2)
                exit()
            else:
                self.programm = programm

        self.programm = programm
        self.start()

    def start(self):

        path = os.getcwd()
        lengh = len(self.programm)
        py = lengh - 3
        py = int(py)
        end = self.programm[py:]

        if end != ".py":
            print(".py files only")
            time.sleep(5)
            os.system("cls")
            self.start()
        else:
            setup = open("setup.py", "w+")
            setup.write("from distutils.core import setup\n")
            setup.write("import py2exe\n")
            setup.write("setup(console=['Payload.py'], options = {'py2exe': {'bundle_files': 1, 'compressed': True}},windows = [{'script': 'Payload.py'}],zipfile = None)")
            setup.close()
            try:
                os.system("python setup.py py2exe > log.log")
            except Exception as fail:
                print("Something happened!" + fail)



