import pymysql
import os
import time
db_host = '127.0.0.1'
db_user = 'root'
db_password = 'hhh123'

backup = '/data/backup/mysql'

time_year = time.strftime('%Y')
time_month = time.strftime('%m')
time_day = time.strftime('%d')

todaybackupdir = backup+'/'+time_year+time_month+time_day
def checkdir():
    if os.path.isdir(todaybackupdir):
        resinfo='文件夹已存在 %s'%todaybackupdir
        print(resinfo)
    else:
        os.makedirs(todaybackupdir)
        resinfo1='文件夹不存在，创建中 %s'%todaybackupdir
        print(resinfo1)

def backup(databasename):
    checkdir()
    backupname = databasename+'_'+time.strftime('%y%m%d')+time.strftime('%H%M')+'.sql'
    try:
        print('开始备份%s '%databasename)
        backupcmd='/usr/bin/mysqldump -u%s -p%s %s  | /usr/bin/gzip > %s/%s.gz' %(db_user,db_password,databasename,todaybackupdir,backupname)
        os.system(backupcmd)
        return "%s 备份成功"%databasename
    except Exception as e:
        return '备份失败 失败原因%s'%e

def main():
    connection=pymysql.connect(host='127.0.0.1',user='root',passwd='hhh123')
    results=[]
    try:
        with connection.cursor() as cursor:
            sql='''show databases'''
            cursor.execute(sql)
            result=cursor.fetchall()
            for i in range(len(result)):
                results.append(result[i][0])

    finally:
        connection.close()


    for databasename in results:
        if databasename != "information_schema" and databasename != "performance_schema" and databasename != "mysql":
            backup(databasename)

if __name__=="__main__":
    main()


