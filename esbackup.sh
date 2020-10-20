#!/bin/bash
source /etc/profile
date=`date +%Y%m%d`
old=`date -d "7 day ago" +"%Y%m%d"`
snap=keyword
folder=/data/backup
result=`curl -XGET http://localhost:9200/_snapshot/${snap}?pretty | grep missing`

echo $result

#exit 1

if [ -z "$result" ]
then
  echo 'snap in'
  curl -XPUT "localhost:9200/_snapshot/$snap/$date?wait_for_completion=true"  -H 'Content-Type: application/json' -d'
    {
    "indices": "*",
    "ignore_unavailable": true,
    "include_global_state": false
    }'
else
  echo 'snapshot is noting'
  curl -XPUT "localhost:9200/_snapshot/$snap" -H 'Content-Type: application/json' -d'
    {
    "type": "fs",
    "settings": {
    "location": "/data/backup",
    "compress":"true"        
    } 
    }'

  curl -XPUT "localhost:9200/_snapshot/$snap/$date?wait_for_completion=true"  -H 'Content-Type: application/json' -d'
    {
    "indices": "*",
    "ignore_unavailable": true,
    "include_global_state": false
    }'
fi


state=`curl -XGET localhost:9200/_snapshot/$snap/$date/_status?pretty | grep SUCCESS`

echo $state


if [ -z "$state" ]
then
  echo "failed"
  echo "$date failed"  >> $folder/back.txt
else
  echo "success"
  echo "$date success" >> $folder/back.txt
fi
curl -XDELETE "localhost:9200/_snapshot/$snap/$old"
