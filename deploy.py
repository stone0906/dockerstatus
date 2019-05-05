# -*- coding: UTF-8 -*-
import sys
import os

if sys.argv.__len__() == 1:
    print("need one arg for name")
    exit(0)
os.chdir("/root/")
with open("docker_info.sh", 'w') as f:
    f.write(r'''#!/usr/bin/env bash
MY_NAME="%s"
ADDR="T_docker"
TMPSTR=`ping ${ADDR} -c 1 | sed '1{s/[^(]*(//;s/).*//;q}'`

for var in $(docker ps -a | awk '{ print $1}' | tail -n +2)
do
ttl=$(sudo docker exec $var cat /sys/class/net/eth0/statistics/rx_bytes)
result=$(sudo docker stats $var  --no-stream | grep -v "CONTAINER ID")
name=$(echo ${result} | awk '{print $2}')
cpu=$(echo ${result} |awk '{print $3}')
mem=$(echo ${result} |awk '{print $7}')
neti=$(echo ${result} |awk '{print $8}')
neto=$(echo ${result} |awk '{print $10}')

curl -G --data-urlencode "name=$MY_NAME" "$TMPSTR:1980/?KEY=hentaidoor&ttl=$ttl&cpu=${cpu:0:-1}&mem=${mem:0:-1}&inet=$neti&onet=$neto&id="$var"_"$name

done''' % (sys.argv[1]))
os.system("echo -e '\n58.33.69.246    T_docker' >> /etc/hosts")
os.system('(echo "* * * * * sleep 50 && /bin/bash /root/docker_info.sh"; crontab -l )| crontab')
os.system('(echo "* * * * * sleep 40 && /bin/bash /root/docker_info.sh"; crontab -l )| crontab')
os.system('(echo "* * * * * sleep 30 && /bin/bash /root/docker_info.sh"; crontab -l )| crontab')
os.system('(echo "* * * * * sleep 20 && /bin/bash /root/docker_info.sh"; crontab -l )| crontab')
os.system('(echo "* * * * * sleep 10 && /bin/bash /root/docker_info.sh" ; crontab -l )| crontab')
os.system('(echo "* * * * * /bin/bash /root/docker_info.sh"; crontab -l )| crontab')
