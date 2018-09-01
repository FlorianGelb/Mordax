import Crypt
import requests
import Compiler

class checkVersion(Crypt.Crypt, Compiler.Compile):

    def setVersion(self, version = 0):
        if version == 0:
            version = 1.0
            return(version)
        else:
            return (version)

    def getLatestVersion(self):
        self.user = "FlorianGelb"
        self.repo = "Mordax"
        path = "version.txt"
        url = 'https://api.github.com/repos/{}/{}/contents/{}'.format(self.user,self.repo,path)
        request = requests.get(url)
        if request.status_code == requests.codes.ok:
            request = request.json()
            content = self.gitb64(request["content"])
            return(content)

    def checkVersion(self):
        self.version = self.setVersion()
        self.content = self.getLatestVersion().rstrip("\\n")
        if self.content.startswith("version = ") and float(self.content[9:]) != self.version:
            print("new version detected")
            return(True)
        else:
            return (False)

    def downloadVersion(self, dat):
        if self.checkVersion() == True:
            path = dat
            if path == "console.py":
                dat = ["console.py", "Client.py", "Crypt.py", "Compiler.py", "CheckVersion.py"]
            if path == "server.py":
                dat = ["server.py", "Client.py", "Crypt.py", "Compiler.py", "CheckVersion.py"]
            for i in dat:
                url = 'https://api.github.com/repos/{}/{}/contents/{}'.format(self.user, self.repo, dat[dat.index(i)])
                request = requests.get(url)
                request_code = request.status_code
                if request.status_code == requests.codes.ok:
                    request = request.json()
                    content = self.gitb64(request["content"])
                    with open(dat[dat.index(i)], "w") as con:
                        con.write(content)
