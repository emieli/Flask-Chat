from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():

    '''Create the application.'''
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_pyfile('config.py') # print(app.config)
    
    ''' Blueprints '''
    from .chat import chat
    app.register_blueprint(chat)

    socketio.init_app(app, cors_allowed_origins = "*")
    return app