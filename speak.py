import subprocess
import paho.mqtt.client as mqtt
import datetime
import time

LAST_COMMAND_TIME = LAST_STATUS_SENT_TIME = datetime.datetime(2018, 11, 28)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe([("hackbot/flow-start", 0)])

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    global LAST_COMMAND_TIME

    # print('on message ' + msg.topic);

    if msg.topic == "hackbot/flow-start":

        cur_time = datetime.datetime.now()

        statusDiff = cur_time - LAST_COMMAND_TIME

        if (statusDiff.seconds > 60):

            subprocess.run(['say', 'hello star'])
            # time.sleep(1)
            # subprocess.run(['say', 'unless you are an L B'])
            # time.sleep(.5)
            # subprocess.run(['say', 'feel free to grab a beer'])



        LAST_COMMAND_TIME = cur_time

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.bigroomstudios.com", 1883, 60)

client.loop_forever()
