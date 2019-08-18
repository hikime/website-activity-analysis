from flask import request, redirect, Blueprint
from ..stream import Consumer, Producer

# Define the blueprint
activity = Blueprint('activity', __name__)


@activity.route('/test/', methods=['GET'])
def test():
    print('Working !!!')
    # producer = Producer()
    # producer.sending()

    # consumer = Consumer()
    # consumer.listen()
