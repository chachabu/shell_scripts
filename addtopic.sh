#!/bin/bash
#关闭logstash
source /etc/profile
logconf=/data/logstash-7.8.1/config/logstash.conf
#logconf=/data/test.txt
logstash=/data/logstash-7.8.1/
kill -9 `ps -ef  |grep logstash |grep -v grep  | awk '{print $2}'`

topic=` /data/kafka-2.6.0/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181 | grep -v __consumer_offsets`
#echo $topic
echo "input {" > $logconf

for add in $topic
do
  echo $add
  echo 'kafka {' >> $logconf
  echo "        bootstrap_servers => \"kafka1:9092\"" >> $logconf
  echo "        topics  => [\""${add}\""]" >> $logconf
  echo "        consumer_threads => 2" >> $logconf
  echo "        decorate_events => false" >> $logconf
  echo "        type => \"$add\"" >> $logconf
  echo "        codec => json" >> $logconf
  echo ' }' >> $logconf
  echo "  " >> $logconf
done

echo "}"  >> $logconf 
echo "filter {
  mutate {
    remove_field => \"@version\"
    remove_field => \"source\"
    remove_field => \"fields\"
    remove_field => \"beat\"
    remove_field => \"offset\"
    remove_field => \"prospector\"
    remove_field => \"input\"
   }
}

output {
  elasticsearch {
    user => elastic
    password => hhh123
    action => \"index\"
    hosts  => \"192.168.244.146:9200\"
    index  => \"%{type}-%{+YYYY.MM.dd}\"
  }

  #stdout{codec => rubydebug }
}"  >> $logconf

#启动logstash
cd $logstash
nohup bin/logstash -f config/logstash.conf &

