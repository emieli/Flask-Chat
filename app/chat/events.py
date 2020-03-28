from flask import session, request, copy_current_request_context
from threading import Lock
from flask_socketio import emit, join_room, leave_room, close_room, rooms, disconnect
from .. import socketio

thread = None
thread_lock = Lock()

messages = []

@socketio.on('connect', namespace='/test')
def on_connect():
    new_message = "{} joined the chat.".format(session['username'])
    messages.append(new_message)
    emit('server_send_messages', "\n".join(messages), broadcast=True)

@socketio.on('disconnect', namespace='/test')
def on_disconnect():
    new_message = "{} has left the chat.".format(session['username'])
    messages.append(new_message)
    emit('server_send_messages', "\n".join(messages), broadcast=True)

@socketio.on('client_send_message', namespace='/test')
def send(message):
    new_message = "{}: {}".format(session['username'], message['data'])
    messages.append(new_message)
    emit('server_send_messages', "\n".join(messages), broadcast=True)
