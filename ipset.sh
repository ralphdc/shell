#!/bin/bash


#使用ipset创建ip地址集合， 使用iptables屏蔽集合里的所有地址；
#https://blog.csdn.net/tycoon1988/article/details/46515535


for ip in `journalctl | grep -E -o "Received disconnect from (.*) port"  | awk '{print $4}' | sort -r | uniq`
do 
	if [ $(ipset list | grep "$ip" | wc -l) -lt 1 ];then
		ipset add banips "$ip/24" > /tmp/ipset.log 2>&1 
	fi
done


for ip in `journalctl | grep -E -o "Failed password for root from (.*) port"  | awk '{print $4}' | sort -r | uniq`
do 
	if [ $(ipset list | grep "$ip" | wc -l) -lt 1 ];then
		ipset add banips "$ip/24" > /tmp/ipset.log 2>&1 
	fi
done



for ip in `journalctl | grep -E -o "Failed password for invalid user (.*) from (.*) port"  | awk '{print $8}' | sort -r | uniq`
do 
	if [ $(ipset list | grep "$ip" | wc -l) -lt 1 ];then
		ipset add banips "$ip/24" > /tmp/ipset.log 2>&1 
	fi
done



if [ $(iptables -L -n | grep banips | wc -l) -lt 1 ];then
	iptables -I INPUT -m set --match-set banips src -p TCP -j DROP
fi 