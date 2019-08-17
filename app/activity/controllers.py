from flask import request, redirect, Blueprint
from app import app

# Define the blueprint
activity = Blueprint('activity', __name__)


@activity.route('/test/', methods=['GET'])
def test():
    print('Working !!!')
