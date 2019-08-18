from flask import Flask
import logging
logging.basicConfig(level=logging.DEBUG)

# Define the WSGI application object
app = Flask(__name__)

# Import a module / component using its blueprint handler variable
from app.activity.controllers import activity

# Register blueprint(s)
app.register_blueprint(activity)

