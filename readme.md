RaspberryPi/ELK Sensing Stream
======================

This is project demonstrates how a RaspberryPi can be used to stream sensor data to an ELK (Logstash/Elasticsearch/Kibana) server. It is adapted from Mark Paluch''s iot-distancemeter at https://github.com/mp911de/iot-distancemeter.

Clone this repo on your RaspberryPi and your ELK server.

```bash
git clone https://github.com/zeluspudding/rasELK.git
```

Logstash/Elasticsearch/Kibana
-----------------------------
You can run this demo also using the ELK-Stack. This way you can visualize the data in a nice way.

Install the ELK Stack using (execute it in the root path of this Git repo, you should use a better host than a RaspberryPi since all components are hungry for Memory and CPU):

```bash
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-get update
sudo apt-get -y install oracle-java8-installer
mkdir -p target
cd target
curl https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.2.zip > elasticsearch-1.3.2.zip
curl https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.zip > logstash-1.4.2.zip
unzip elasticsearch-1.3.2.zip
unzip logstash-1.4.2.zip
cd elasticsearch-1.3.2/bin
chmod a+x elasticsearch
./elasticsearch &
cd ../..
cd logstash-1.4.2/bin
chmod a+x logstash
./logstash agent -f ../../../logstash.conf &
./logstash-web &
curl -XPUT 'http://localhost:9200/kibana-int/'
curl -XPUT --data-binary '@../../../dashboard-source.json' 'http://localhost:9200/kibana-int/dashboard/Sonic%20Distancemeter'
```

Now your server stack is running. Go to your RaspberryPi and adopt `JSON_HOST` in `distancemeter_json.py` so the Python
script knows where to send the JSON objects using TCP. Then run:

```bash
$ sudo python distancemeter_json.py
```

Your RaspberryPi will send every 0.2sec a message over the line. At this point open your browser. Kibana runs on port 9292,
iot-distancemeter
======================

This is project demonstrates how a RaspberryPi can be used to stream sensor data to an ELK (Logstash/Elasticsearch/Kibana) server. It is adapted from Mark Paluch''s iot-distancemeter at https://github.com/mp911de/iot-distancemeter.



Clone this repo on your RaspberryPi and your host where your server (Logstash) is hosted.

```bash
git clone https://github.com/zeluspudding/rasELK.git
```

```

Logstash/Elasticsearch/Kibana
-----------------------------
You can run this demo also using the ELK-Stack. This way you can visualize the data in a nice way.

Install the ELK Stack using (execute it in the root path of this Git repo, you should use a better host than a RaspberryPi since all components are hungry for Memory and CPU):

