#/bin/bash
export RSYNC_PASSWORD=Zhendao_2020Dao
source /etc/profile
yum -y install rsync

if [ ! -n "$1" ]; then
	echo "输入目标服务器"
	exit 1
else

	for i in `cat /opt/mig.txt`
	do
	file=`echo $i|sed -r 's#[^/]+$##'`
	echo $i
	echo $file
	rsync -avz --delete $i $1:$file
	done
fi
rsync -avz --delete /var/spool/cron/root  $1:/var/spool/cron/
rsync -avz --delete /usr/local/nginx/conf $1:/usr/local/openresty/nginx/


