from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

clients = []

@sock.route('/ws')
def websocket(ws):
    clients.append(ws)
    while True:
        data = ws.receive()
        for client in clients:
            if client != ws:
                client.send(data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
