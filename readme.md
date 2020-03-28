
# Flask Chat
This is a project setup to help beginners get started with Flask-socketio. The goal is provide a sample website that show how Flask can be used to build a websocket website following current best practices (to the best of my knowledge).
## What the website does
- The main goal of the website is to provide a simple chat.
- Using blueprints, we show how the page can be expanded easily. There is only one blueprint "chat" in the example.
- The website is made pretty using Bootstrap, you can find more info about it here: https://getbootstrap.com/
## How to install
This guide assumes you have sudo access to a Debian 10 machine. Commands may otherwise be different.
### 1. Make sure Debian has the required dependencies
    sudo apt update
    sudo apt install git python3-pip python3-venv

We use git to clone this repo to a local folder on your device. Pip is used to download the required python modules. Venv is used to run the flask server in a python virtualenv to keep dependencies separate from other projects on the same machine.

### 2. Clone the repo and enter the folder
	user@server:~$ git clone https://github.com/emieli/Flask-Chat.git
	Cloning into 'Flask-Chat'...
	Unpacking objects: 100% (24/24), done.
	user@server:~$ cd Flask-Chat/
### 3. Build and enter the Virtualenv
	user@server:~/Flask-Chat$ python3 -m venv venv
	user@server:~/Flask-Chat$ source venv/bin/activate
	(venv) user@server:~/Flask-Chat$ deactivate # to leave the venv
### 4. Install the required python modules inside the venv
	user@server:~/Flask-Chat$ venv/bin/python3 -m pip install -r requirements.txt
	Successfully installed flask==1.1.1 flask-socketio==4.2.1 eventlet==0.25.1 wtforms==2.2.1
### 5. Start the flask server from the venv
	user@server:~/Flask-Chat$ venv/bin/python3 app.py
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 326-749-762
    (15180) wsgi starting up on http://0.0.0.0:5000
### 6. All done!
You should now be able to use your browser on the local or a nearby device to reach the webpage on port 5000.
http://\<your-debian-ip\>:5000

## Recommended actions
Recommended actions before taking the site into 'production':
### Edit the instance/config.py file
Find the config.py file in the instance folder and change the SECRET_KEY to a random string. This is for encrypting session cookies etc, so it is vital that noone can read this. The instance folder should also be in the .gitignore file so that it is not viewable, but I am keeping it here for clarity.
You should also set DEBUG to False if you don't need it enabled.

### Change cors_allowed_origins
CORS is a security mechanism to stop other sites from sending weird requests to your site via the users browser. Right now the "cors_allowed_origins" in app/__init__.py is set to "*", but this should be changed to your url "http://\<your-debian-ip\>:5000" for maximum security. If this is configured incorrectly, the webserver will return a "400 BAD REQUEST" and the websocket will not connect properly.
