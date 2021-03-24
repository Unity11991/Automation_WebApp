from flask import Flask,request,render_template
import subprocess
import socket
from threading import Thread

app = Flask(__name__)


@app.route('/',methods=["GET"])
def hello_world():
    cname = subprocess.getoutput("date /t")
    return render_template("HomePage1.html" , cname=cname)

@app.route('/tech.html',methods=["GET"])
def tech():
    data=request.args.get("command")
    if("chat" in data):
        return render_template("chat.html")
    elif("AWS" in data):
        return render_template("AWS_Lander.html")
    else:
        return render_template("tech.html", mydata = subprocess.getoutput(data) )

@app.route('/User_loged_IN.html', methods=["GET"])
def user_logged():
    name = request.args.get("name")
    email = request.args.get("email")
    message = request.args.get("msg")

    cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = "192.168.118.143"
    port = 2222

    cs.connect((ip,port))
    while True:
        def send_data():
                cs.sendall(name.encode())
    while True:
        def recv_data():
            while True:
                data = cs.recv(1000)
                print(data.decode())
    t=Thread(target=recv_data)
    t.start()
    send_data()
    cs.close()
    return render_template("User_loged_IN.html", myname=name,myemail=email)

@app.route("/AWS-Lander.html", methods=["GET"])
def aws():
    Acesskey = request.args.get("command")
    SecretKey = request.args.get("command1")

    print(Acesskey)
    print(SecretKey)

    return render_template("AWS_Lander.html", Acesskeys=Acesskey, SecretKeys=SecretKey)
if __name__ == '__main__':
    app.run()
