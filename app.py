from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import json

import paho.mqtt.client as paho
import time

app = Flask(__name__)
CORS(app)

# app.config['CORS_HEADERS'] = 'Content-Type'

# cors = CORS(app, resources={r"/send_message": {"origins": "http://localhost:port"}})

# cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})
# app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


def on_publish(client, userdata, mid):
    print("mid: "+str(mid))


def publish_message(username, password, server, port, topic, message):
    success = 0
    client = paho.Client()
    client.username_pw_set(username, password)
    client.connect(server, port)
    client.loop_start()
    (rc, mid) = client.publish(topic, message, qos=1)
    client.disconnect()
    success = 1
    return(success)

@app.route('/')
def index():
    return render_template('index.html')
    # return 'Hello world'

@app.route('/send_message', methods=['POST'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
@cross_origin()
def send_message():
    if request.method == 'POST':
        # print(json.loads(request.data))
        print(request.get_json())
        print(request.form.to_dict())
        print('hello')

        request_object = json.loads(request.data)
        topic = request_object['topic']
        message = request_object['message']
        username = request_object['username']
        password = request_object['password']
        server = request_object['server']
        port = request_object['port']
        #
        # # topic = "uniqueID/topic"
        # # default_message =  "Johanna!\nElizabeth!\nMommy!"
        #
        publish_message(username, password, server, port, topic, message)
        print(request.data)

    else:
        print('Invald method')
    return(request.data)
    # return ('{}')


@app.errorhandler(500)
@cross_origin()
def internal_error(error):

    return "500 error"

@app.errorhandler(404)
@cross_origin()
def not_found(error):
    return "404 error",404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)



# import paho.mqtt.client as paho
# import time
# client = paho.Client()
# def on_publish(client, userdata, mid):
#     print("mid: "+str(mid))
# client.username_pw_set("rgrttlps", "ExgIbmBaXDVD")
# client.connect("m13.cloudmqtt.com", 13635)
# client.loop_start()
# (rc, mid) = client.publish("uniqueID/topic", "Johanna!\nElizabeth!\nMommy!", qos=1)

