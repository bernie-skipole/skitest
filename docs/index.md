# Container build documentation

This documents creating a container on a server, for the full build of the server, see

[https://bernie-skipole.github.io/webparametrics/](https://bernie-skipole.github.io/webparametrics/)

On server webparametrics.co.uk, as user bernard

lxc launch ubuntu:20.04 skitest

lxc list

This gives container ip address 10.105.192.227

lxc exec skitest -- /bin/bash

apt-get update

apt-get upgrade

apt-get install python3-pip

Then as root in tester:

adduser bernard

record the password


## Install git, and clone skitest repository

Then as user bernard create an ssh key

runuser -l bernard

ssh-keygen -t rsa -b 4096 -C "bernie@skipole.co.uk"

copy contents of .ssh/id_rsa.pub to github

clone any required repositories

git clone git@github.com:bernie-skipole/skitest.git

copy /home/bernard/skitest to /home/bernard/www without the .git and .gitignore
(this rsync command can be used to update /www whenever git pull is used to update /skitest)

rsync -ua --exclude=".*" ~/skitest/ ~/www/

The skitest Python program requires the skipole package
and waitress

python3 -m pip install --user skipole

Python3 -m pip install --user waitress

It should now be possible to run skitest

python3 ~/www/skitest/code/skitest.py

And you should get the message

Serving skitest on port 8000

Use ctrl-c to exit, and set up a service to run this automatically

## Install skitest.service

as root, copy the file

cp /home/bernard/www/skitest.service /lib/systemd/system

Enable the service

systemctl daemon-reload
systemctl enable skitest.service
systemctl start skitest

This starts /home/bernard/www/skitest/code/skitest.py on boot up.

The site will be visible at.

[https://webparametrics.co.uk/test](https://webparametrics.co.uk/test)



