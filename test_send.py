import os, sys, json
import requests, time
for i in xrange(1000000):
    r = requests.post('http://192.168.0.68:1234/send_message', data = json.dumps({"username": "rgrttlps", "password":"ExgIbmBaXDVD", "port":13635, "server":"m13.cloudmqtt.com", "topic":"uniqueID/topic","message":" "*(i % 10)  + 'Johanna\n' + ' '*(i % 10) + "Katrina\n" + ' '*(i % 10) + "Kwong"}))
#    print r.content
    time.sleep(0.5)
