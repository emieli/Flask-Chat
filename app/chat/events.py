from flask import session, request, copy_current_request_context
from threading import Lock
from flask_socketio import emit, join_room, leave_room, close_room, rooms, disconnect
from .. import socketio

messages = []

@socketio.on('connect')
def on_connect():
    new_message = f"{session['username']} joined the chat."
    messages.append(new_message)
    emit('server_send_all_messages', "\n".join(messages), broadcast=True)
    return

@socketio.on('disconnect')
def on_disconnect():
    new_message = f"{session['username']} has left the chat."
    messages.append(new_message)
    emit('server_send_message', new_message, broadcast=True)

@socketio.on('client_send_message')
def send(message):
    new_message = f"{session['username']}: {message}"
    messages.append(new_message)
    emit('server_send_message', new_message, broadcast=True)