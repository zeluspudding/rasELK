__author__ = 'consious'

import socket
import json
import time
from cputempmeter import getCPUtemperature

# Logstash TCP/JSON Host
JSON_PORT = 9400
JSON_HOST = '104.131.22.155'

CM_PER_SEC_AIR = 34300


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((JSON_HOST, JSON_PORT))

        while True:
            temperature = getCPUtemperature()
            data = {'message': 'temperature %.1f cm' % temperature, 'temperature': temperature, 'hostname': socket.gethostname()}

            s.send(json.dumps(data))
            s.send('\n')
            print ("Received temperature = %.1f C" % temperature)
            time.sleep(0.2)

    # interrupt
    except KeyboardInterrupt:
        print("Programm interrupted")
