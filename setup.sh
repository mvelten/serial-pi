#!/bin/sh
###
# shell script to install serial-pi on a Raspberry Pi
###

if [ ! -f serialpiconfig.py ]
then
echo "Please create confile file serialpyconfig.py first"
exit 1
fi

# install screen and create folder
if [ ! -x /usr/bin/screen ]
then
    apt-get update && apt-get install screen -y
fi
mkdir -p /usr/local/bin/

cp serial-pi.py /usr/local/bin/serial-pi.py
cp serialpiconfig.py /usr/local/bin/serialpiconfig.py

# create user console
if ! grep -q console /etc/passwd
then
    useradd -s /usr/local/bin/serial-pi.py -m -d /home/console -c "serial console" console
    echo "Enter new password for user console"
    passwd console
fi

# grant admin rights without password to console
if ! grep -q console /etc/sudoers
then
    echo "console ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
fi