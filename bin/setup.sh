#!/usr/bin/env bash

# RPM prerequisites
yum -y install gcc zlib-devel openssl-devel bzip2-devel gcc-c++ readline-devel git wget python vim ntp


if [ ! `which pip 2> /dev/null` ]
then
  # install pip (http://www.pip-installer.org/en/latest/installing.html)
  wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python
  wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py -O - | python
fi

# install stuff from PyPI
pip install virtualenv
pip install ipython

# NTP pool (http://www.cyberciti.biz/faq/howto-install-ntp-to-synchronize-server-clock/)
ntp_profile(){
cat <<EOF
server 0.rhel.pool.ntp.org
server 1.rhel.pool.ntp.org
server 2.rhel.pool.ntp.org
EOF
}
ntp_profile > /etc/ntp.conf
service ntpd restart

my_profile(){
cat<<EOF
alias l="ls -la"
EOF
}

my_profile > ~/.profile

# TODO add nginx to repo and install

#cat /vagrant/bin/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

cd /vagrant/
add_pypi_packages(){
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
}
[ ! -f venv ] && add_pypi_packages
