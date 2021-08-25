#!/bin/bash

#sql backup

DATE=`date +'%Y-%m-%d'`
DB_LIST=`mysql -uroot  -e  'show databases' | grep -v test | grep -v Database |  grep -v performance_schema |grep -v  information_schema | grep -v _schema | grep -v mysql`
#DB_LIST=`mysql -h10.0.0.195 -uroot -p'ucloud.cn' -e 'show databases;'|grep -v -E 'information_schema|performance_schema|sys|Database'`
DB_BACKUP_DIR="/data/back/mysql/$DATE"
mkdir -p $DB_BACKUP_DIR
if [ ! -d $DB_BACKUP_DIR ];then
        mkdir -p $DB_BACKUP_DIR
        fi

for i in $DB_LIST
do
mysqldump --opt --force  -uroot  --log-error=/tmp/mysqldumpzmtdlzd_error_log --hex-blob --master-data=2 --single-transaction -R --events $i |gzip >$DB_BACKUP_DIR/$i.sql.gz
done
