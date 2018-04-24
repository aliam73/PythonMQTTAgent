#!/usr/bin/env python

from time import sleep
from CloudingThingsPythonAgent.pythonMqttAgent import CloudingThingsMqttClient


gtw_config={
   'client': 'demo',
   'serial': 'demo',
   'credential_file': 'path_to_crt_file.crt',
   'broker': '5.135.83.28',
   'transport': 'ssl',
   'port': 8883,
   'auto_reconnect': True
}

class MqttAgent(CloudingThingsMqttClient):

    def on_message(self, cl, userdata, msg):
        '''
            The callback for when a PUBLISH message is received from the server.
            Call do method of related actuator
            Add custom code to treat messages
        '''
        print msg.payload


if __name__ == "__main__":
    data={
        'loop': 0
    }
    agent = MqttAgent(gtw_config)
    agent.start_mqtt_client()
    print 'Agent started'
    while True:
        data['loop'] = data.get('loop')+1
        agent.publish(data)
        print 'Message published'
        sleep(5.0)
    
