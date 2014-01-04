#!/usr/bin/env bash

# RPM prerequisites
yum -y install gcc gcc-c++ zlib-devel openssl-devel bzip2-devel readline-devel git wget python python-devel mysql mysql-devel vim ntp


cat <<EOF > /etc/yum.repos.d/nginx.repo
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/rhel/6/\$basearch/
gpgcheck=0
enabled=1
EOF

yum -y install nginx


if [ ! `which pip 2> /dev/null` ]
then
  # install pip (http://www.pip-installer.org/en/latest/installing.html)
  wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python
  wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py -O - | python
fi

# install the only global from PyPI
pip install virtualenv

# NTP pool (http://www.cyberciti.biz/faq/howto-install-ntp-to-synchronize-server-clock/)
cat <<EOF > /etc/ntp.conf
server 0.rhel.pool.ntp.org
server 1.rhel.pool.ntp.org
server 2.rhel.pool.ntp.org
EOF
service ntpd restart

cat <<EOF > $HOME/.profile
alias l="ls -la"
EOF

# TODO add nginx to repo and install
cat /vagrant/bin/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

cd /vagrant/
add_pypi_packages(){
  virtualenv venv
  source ./venv/bin/activate
  pip install -r requirements.txt
}
[ ! -d venv ] && add_pypi_packages
