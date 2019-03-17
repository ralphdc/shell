#!/bin/bash


#centos7 系统开发环境搭建；

function get_current_time_stamp()
{
echo `date "+%Y/%m/%d %H:%M:%S"`
}

function send_error()
{
echo -e "\e[1;45m [ Error ] `get_current_time_stamp` - $1 -\e[0m"
}

function send_success()
{
echo -e "\e[1;32m [ Success ] `get_current_time_stamp` - $1 -\e[0m"
}

function send_info()
{
echo -e "\e[1;34m [ Info ] `get_current_time_stamp` - $1 -\e[0m"
}

function send_warn()
{
echo -e "\e[1;33m [ Warn ] `get_current_time_stamp` - $1 -\e[0m"
}




function install_php7()
{
	
}


function install_mariadb()
{
	yum install rsync nmap lsof perl-DBI nc
	yum install boost-program-options*
	yum install libaio*
	rpm -ivh jemalloc-3.6.0-1.el7.x86_64.rpm
	rpm -ivh jemalloc-devel-3.6.0-1.el7.x86_64.rpm
	rpm -ivh galera-25.3.25-1.rhel7.el7.centos.x86_64.rpm
	rpm -ivh MariaDB-10.3.13-centos73-x86_64*.rpm
	
	
}