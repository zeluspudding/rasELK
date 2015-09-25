import socket, json, time
from cputempmeter import getCPUtemperature
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': '104.131.22.155', 'port': 9200}])

if __name__ == '__main__':
    try:
        i = 1 #Prepare to iterate over samples
        while True:
            temperature = getCPUtemperature()
            data = {'message': 'temperature %.1f cm' % temperature, 'temperature': temperature, 'hostname': socket.gethostname()}
            print ("Received temperature = %.1f C" % temperature)
            es.index(index='raspi1', doc_type='stimuli', id=i, body=json.loads(data))
            es.index(index='raspi2', doc_type='stimuli', id=i, body=json.dumps(data))
            es.index(index='raspi3', doc_type='stimuli', id=i, body=data)
            i=i+1
            time.sleep(0.2)
    
    # interrupt
    except KeyboardInterrupt:
        print("Programm interrupted")
