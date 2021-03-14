from flask import Flask,request,render_template
import subprocess
import socket
from threading import Thread

app = Flask(__name__)


@app.route('/',methods=["GET"])
def hello_world():
    cname = subprocess.getoutput("date /t")
    return render_template("HomePage.html" , cname=cname)

@app.route('/tech.html',methods=["GET"])
def tech():
    data=request.args.get("command")
    if("chat" in data):
        return render_template("chat.html")
    else:
        return render_template("tech.html", mydata = subprocess.getoutput(data) )

@app.route('/chat.html', methods=["GET"])
def chatapp():
    """server = socket.socket()
    ip = "192.168.56.1"
    port = 2222
    server.connect(("ip",port))
    server.send(name)"""
    return render_template("chat.html")
"""@app.route('/chatFront.html', methods=["GET"])
def friend_circle():
    return render_template("chatFront.html")
"""
@app.route('/User_loged_IN.html', methods=["GET"])
def user_logged():
    name = request.args.get("name")
    email = request.args.get("email")
    message = request.args.get("msg")
    """print("Got a User Details")
    server = socket.socket()
    ip = "192.168.222.143"
    port = 2222
    server.connect((ip,port))

    def send_data():
        while True:
            server.sendall(message.encode())
            print("msg send successfully")
    def recv_data():
        while True:
            data = server.recv(1024)
            print(data.decode())
    t = Thread(target=recv_data)
    t.start()
    send_data()
    server.close()"""

    return render_template("User_loged_IN.html", myname=name,myemail=email)

@app.route('/conversation.html',methods=["GET"])
def converstation():
    message = request.args.get("msg")
    print("Got a User Details")
    server = socket.socket()
    ip = "192.168.222.143"
    port = 2222
    server.connect((ip, port))

    def send_data():
            server.sendall(message.encode())
            print("msg send successfully")

    def recv_data():
        message = []
        while True:
            data = server.recv(1024)
            message.append(data)
    t = Thread(target=recv_data)
    t.start()
    send_data()
    server.close()
    return render_template("conversation.html",msg=message)
if __name__ == '__main__':
    app.run()
