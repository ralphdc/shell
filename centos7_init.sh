#!/bin/bash

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







#init os
function init_os()
{

	yum -y update
	
	if [ -f /etc/pam.d/su ];then
		if [ $(sed -n '/^#auth\s*required\s*pam_wheel.so use_uid/p'  | wc -l) -eq 1 ];then
			send_info "backup file..."
			cp /etc/pam.d/su /etc/pam.d/su.bak
			send_info "uncomment wheel group authentication..."

		fi
	else
		send_warn " [404] /etc/pam.d/su not found..."
	fi
	
	#create admin group
	if [ $(grep admin /etc/group | wc -l) -lt 1 ];then
		send_info "add admin group..."
		groupadd admin
		if [ $? -eq 0 ];then
			send_success "admin group add OK!"
		else
			send_error "create admin group Failed!"
		fi
	else
		send_info "OK! admin group has been created!"
	fi

	#create admin user
	if [ $(grep admin /etc/passwd | wc -l) -lt 1 ];then
		send_info "add admin user..."
		useradd -g admin -G wheel  -d /home/admin -m admin 
		if [ $? -eq 0 ];then
			send_success "create admin user  OK!"
		else
			send_error "create admin user Failed!"
		fi
	else
		send_info "OK! admin user has been created!"
	fi






}


#install php
function install_php()
{

	send_info "add www group and user for PHP..."
	grouadd www 
	useradd -g www -d /home/www -m www 

	send_info "create php7 directory..."
	if [ ! -d /usr/local/php7 ];then
		mkdir /usr/local/php7
	fi
	if [ ! -d /usr/local/php7/etc ];then
		mkdir /usr/local/php7/etc
	fi
	
	send_info "begin to install dependency packages..."
	yum install -y gcc gcc-c++  make zlib zlib-devel pcre pcre-devel  libjpeg libjpeg-devel \
	libpng libpng-devel freetype freetype-devel libxml2 libxml2-devel glibc glibc-devel glib2 \
	glib2-devel bzip2 bzip2-devel ncurses ncurses-devel curl curl-devel e2fsprogs e2fsprogs-devel \
	krb5 krb5-devel openssl openssl-devel openldap openldap-devel nss_ldap openldap-clients openldap-servers \
	libxslt libxslt-devel

	
	

}


#install mysql
function install_mysql()
{


}


function install_nginx()
{


}

if [ ! -f /etc/redhat-release ];then
	send_error "OS does not match! === Centos7+ ==="
	exit 
fi