from flask import session, request
from flask_socketio import emit, join_room, leave_room
from .. import socketio


from flask_socketio import join_room, leave_room

@socketio.on('connect')
def connect():
	print("Recieved request from socket = " + request.sid)
	emit('message', {'data': 'l'})