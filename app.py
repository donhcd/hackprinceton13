#from flask import Flask
import socket
#app = Flask(__name__)

#@app.route("/")
def hello():
    return "Hello World!"

# if __name__ == "__main__":
#     app.run(host='0.0.0.0')
if __name__ == "__main__":
    HOST = ''
    PORT = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    while 1:
        s.listen(1)
        conn, addr = s.accept()
        print 'Connected by', addr
        while 1:
            data = conn.recv(1024)
            print data
            #print 'data was len=',len(data)
            if not data: break
        conn.close()
