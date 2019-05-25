from flask import Flask, render_template
from flask_socketio import SocketIO,send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    to_client=dict()
    if message=="new_connect":
        to_client['message']='Chatting Started'
        to_client['type']='connect'
    else:
        to_client['message']=message
        to_client['type']='normal'
    send(to_client,broadcast=True)
if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)

    #http://localhost:5000로 수동 연결 해주어야 함