# Import libraries
import os

from flask import Flask, redirect, render_template, session, url_for
from flask_socketio import SocketIO, emit, join_room

# Create flask app
app = Flask(__name__, static_folder='static')
app.secret_key = os.urandom(12).hex()

# Create socket
socketio = SocketIO(app, cors_allowed_origins='*', threading='gevent')

@socketio.on('join')
def on_join(room_name):
    join_room(room_name)
    session['room_name'] = room_name

@socketio.on('message')
def send_message(message):
    emit('message', message, room=session['room_name'])

@app.route('/')
def default():
    return redirect(url_for('join'))

@app.route('/join_room')
def join():
    return render_template('join_room.html')

@app.route('/message/<room_name>')
def message(room_name):
    return render_template('message.html', room_name=room_name)

if __name__ == '__main__':
    app.run(debug=True)