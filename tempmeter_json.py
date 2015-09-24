__author__ = 'mp911de'

import socket
import json
import time
from temperaturemeter import get_temperature,cleanup

# Logstash TCP/JSON Host
JSON_PORT = 9400
JSON_HOST = '192.168.55.34'

CM_PER_SEC_AIR = 34300


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((JSON_HOST, JSON_PORT))

        while True:
            temperature = get_temperature()
            data = {'message': 'temperature %.1f cm' % temperature, 'temperature': temperature, 'hostname': socket.gethostname()}

            s.send(json.dumps(data))
            s.send('\n')
            print ("Received temperature = %.1f cm" % temperature)
            time.sleep(0.2)

    # interrupt
    except KeyboardInterrupt:
        print("Programm interrupted")
        cleanup()
