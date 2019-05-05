#!/usr/bin/env bash
MY_NAME="香港微软云"
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

doneYou have new mail in /var/spool/mail/root
