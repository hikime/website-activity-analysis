from flask import Flask

# Define the WSGI application object
app = Flask(__name__)

# Import a module / component using its blueprint handler variable
from app.activity.controllers import activity

# Register blueprint(s)
app.register_blueprint(activity)

