from flask import Flask, render_template, session
from flask_socketio import SocketIO, join_room, emit

app = Flask(__name__, static_folder='static')
socketio = SocketIO(app, cors_allowed_origins='*', threading='gevent')

@socketio.on('join')
def on_join(room_name):
    join_room(room_name)
    session['ROOM_NAME'] = room_name

@socketio.on('message')
def send_message(message):
    emit('message', message, room=session['ROOM_NAME'])

@app.route('/message/<room_name>')
def message(room_name):
    return render_template('message.html', room_name=room_name)

if __name__ == '__main__':
    app.run(debug=True)