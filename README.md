# June 5th 2021

## Google Docs
[This document contains the Hardware and Software Specifications](https://docs.google.com/document/d/1VmVc4CmjYzYFPzCeiBg8k-KrPtAwDRACMsuuZYY_06A/edit)

# SOFTWARE AND HARDWARE REQUIREMENTS FOR GAME BIT SYSTEMS

### Chapter one 

### Background
Owners of game station can only monitor their stations when present or else entrust someone

### Chapter two

### Problem statement
Inconsistent tracking of the game station earnings which could be solved by computerised tracking 

### Objectives of the project

### General objective of the project
To provide a new way of game station earnings tracking

### Specific objectives 

+ To study the current system being used at game stations.
+ To identify the requirements for developing an a bit game system to counter the current system
+ To develop the bit game system
+ To test and validate the bit game system to establish whether it addresses the general objective.

### Chapter three

### Requirements specification

Specific requirements are split into two that is user and system requirements.

+ **User Requirements**
The Bit Game System will be accessible to the bit game users.

+ **System Requirements**
These are requirements for the system to be able to perform its functionality efficiently and effectively.

#### Functional requirements
+ Time the game station has been active on a specific day
+ Detect presence of a client on a particular console
+ Store presence data on a particular console
+ Display presence data on a particular console

#### Non-Functional requirements
+ The bit game system should be upload its data 5 times a day.


### Chapter four 

### System designs


# Installing Ubuntu Server on Raspberry pi 3
+ First, insert the microSD card into your computer.

If you are on Ubuntu, you can run:

sudo snap install rpi-imager

it takes the rpi-imager 40 minutes plus to write ubuntu 21.04 server to the sd card

Open the imager and follow the prompts

This takes up some time so what i did was to download the ubuntu server 20.04.2 meant for raspberry pi 3 

Right click on the "Disk image Writer" 

Restore the intended disk

With the SD card still inserted in your laptop, open a file manager and locate the “system-boot” partition on the card. It contains initial configuration files that load during the first boot process.

Edit the network-config file to add your Wi-Fi credentials. 

### **Note: wifi name must be enclosed in quotation marks**


### Raspberry pi ubuntu server 21.04 command-line login
ubuntu login :ubuntu
password : ubuntu



After that you will be prompted to create a new password and then retype the new password


### using nmap to find the ip address of the raspberry pi

i used nmap tool

$ nmap -sn 192.168.43.0/24

### using open shh to remotely connect to the raspberry pi
Logging in from other computers

Although SSH has many uses, its main job is to provide access to a command-line over a network. Even if you are installing SSH for completely different reasons, it's best to get command-line access before you try anything more complicated. 

To login remotely using ssh i used my terminal

$ ssh ubuntu@192.168.43.35

The text below appears whenever i login to the raspberry pi using ssh

```bash
The authenticity of host '192.168.43.36 (192.168.43.36)' can't be established.
ECDSA key fingerprint is SHA256:haZoIbxB4bbnngdUS6jjn+yluq+9XEpWv4R6vvZ5Awk.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.43.36' (ECDSA) to the list of known hosts.
ubuntu@192.168.43.36's password: 
Welcome to Ubuntu 21.04 (GNU/Linux 5.11.0-1009-raspi aarch64)
```

### upgrading ubuntu

$ sudo apt upgrade
This take one full hour 

### install ubuntu desktop

$ sudo apt update
$ sudo apt upgrade

$ sudo apt install xubuntu-desktop(this one hour to download and another hour to unpack)

$ sudo reboot

### uninstall the desktop

sudo apt remove xubuntu-desktop
sudo apt autoremove xubuntu-desktop
sudo apt purge xubuntu-desktop

### Removing gnome
sudo apt-get remove --purge gnome*
sudo apt autoremove

### Enable auto login in console

Enter the command **sudo raspi-config**. Scroll down to **Boot Options** and select **Console Autologin**. Then exit the configuration menu and reboot.

#### Next Step

I made this file: /etc/systemd/system/getty@tty1.service.d/autologin.conf
And put this in it:


```
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin username --noclear %I 38400 linux
```

After that, i runned this:

$ sudo systemctl enable getty@tty1.service

### installing git
$ sudo apt install git

### copy files remotely via shh using SCP "secure copy" utility

$ scp requirements.txt ubuntu@192.168.43.35:/home/ubuntu/venvs/tangibleai


### Clone Github repository
$ git clone repository url

### Get an email about the time and date raspberry pi was powered on

#### Requirements
+ Gmail account for development
+ cron job
+ smtplib module
+ ssl module

The time and date will be shown by the email.

```python
import smtplib, ssl

#email 

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "nicobwan@gmail.com"  # Enter your address
receiver_email = "offdutymanager@gmail.com"  # Enter receiver address
# password = input("Type your password and press enter: ")
password = "xxxxx"
message = """\
Subject: Raspberry Vivian

I have been powered on."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


```

### installing dhcp server on my laptop to statically assign an ip to the raspberry pi

sudo apt install isc-dhcp-server -y
### create an shell script to run the python script to send email


### create a cron job to run the python script to send email.

### Code a cron job to start whenever the raspberry pi is started


#### To set up a Gmail address for testing your code, do the following:
+ Create a new Google account.
+ Turn Allow less secure apps to ON. Be aware that this makes it easier for others to gain access to your account.

### Setting time on ubuntu server

    Search for your timezone

timedatectl list-timezones

    Set your timezone

sudo timedatectl set-timezone America/Toronto

    Enable timesyncd

sudo timedatectl set-ntp on



## Setup Django 
https://django.readthedocs.io/en/stable/

## Setup Users in Django User Management

Start by the disabling the users inside settings.py>AUTH_PASSWORD_VALIDATORS


## Create a dashboard view

## Create an index page

## Work With Django User Management
Django has a lot of user management–related resources that’ll take care of almost everything, including login, logout, password change, and password reset. Templates aren’t part of those resources, though. You have to create them on your own.

inside the apps>urls.py>urlpatterns add the element below
url(r"^accounts/", include("django.contrib.auth.urls")),


accounts/login/ is used to log a user into your application. Refer to it by the name "login".

accounts/logout/ is used to log a user out of your application. Refer to it by the name "logout".

accounts/password_change/ is used to change a password. Refer to it by the name "password_change".

accounts/password_change/done/ is used to show a confirmation that a password was changed. Refer to it by the name "password_change_done".

accounts/password_reset/ is used to request an email with a password reset link. Refer to it by the name "password_reset".

accounts/password_reset/done/ is used to show a confirmation that a password reset email was sent. Refer to it by the name "password_reset_done".

accounts/reset/<uidb64>/<token>/ is used to set a new password using a password reset link. Refer to it by the name "password_reset_confirm".

accounts/reset/done/ is used to show a confirmation that a password was reset. Refer to it by the name "password_reset_complete

## Create a login page
For the login page, Django will try to use a template called registration/login.html.

## Create a logout page 
registration/logged_out.html.

## Change Passwords
1.registration/password_change_form.html to display the password change form

2.registration/password_change_done.html to show a confirmation that the password was successfully changed

## How am i going to connect the user table to the other tables?
Am going to extend the User table and make it as a foreign key in the pool table because i want each user to store there own data and see , their own data.

First i will import user model.

from django.contrib.auth.models import User

Then create a field in the pool_table
user = models.OneToOneField(User, on_delete=models.CASCADE)

## What do i want the user to see on the dashboard
Games played in a day
-how are we getting the games played 

By the word dashboard , it means that am going to be dealing with views , so the logic is going to be in the views.py module

Pull the user 
grab the user whose data that i want to show

Pull his or table

Pull the data

Show the data

so i will grab data for a specfic date first 

Then loop through it and code that for every input in the whole range
if input status is equal 1 then add it to pockets variable

if the pockets variable is equal to 15 its means that one game has been played 

one game is equal to 50/=


Money collected in a day

## What tables database tables am i going to have?
Pool table
To hold the location , table name

Action table
To hold 
'id', 'status', 'date', 'time'

So a user has a pool table and his pooltable played on , so when am registering , i can combine a user to have the user's details and the pool table that they are having .

## Combination of user table and the pool_table


## Make raspberry pi talk to arduino board
```python
import datetime
from datetime import datetime
import serial
from time import time, ctime

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
#now = datetime.datetime.now()
#dateTimeObj = datetime.now()
t = time()
ti= ctime(t)
while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print ( ":" ,data)

```


### Requirements
+ serial module(**pip3 install pyserial**)

## Change the database from sqlite3 to mysql 

```bash
sudo apt install mysql-server

```
In order to use MySQL with our project, we will need a Python 3 database connector library compatible with Django. So, we will install the database connector, mysqlclient,

First ensure that you have python3-dev installed
```bash
sudo apt install python3-dev
```
We can now install the necessary Python and MySQL development headers and libraries:

```bash
sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev

```

```bash
pip install mysqlclient
```
### Create the database
Now that the skeleton of my Django application has been set up and mysqlclient and mysql-server have been installed, we will to need to configure my Django backend for MySQL compatibility.

Log in via the MySQL root with the following command:

```mysql
sudo mysql -u root
```
### create a mysql user to use the bit_game database
```mysql
CREATE USER 'jacob'@'%' IDENTIFIED WITH mysql_native_password BY 'vivian@123';

```
### Next, let the database know that our "jacob" should have complete access to the database we set up:
```mysql
GRANT ALL ON bit_game.* TO 'jacob'@'%';
```

### Flush the privileges so that the current instance of MySQL knows about the recent changes we’ve made:
```mysql
FLUSH PRIVILEGES;
```
## Add the MySQL Database Connection to your Application
Note: It is important to remember that connection settings, according to the Django documentation, are used in the following order:
+ OPTIONS
+ NAME, USER, PASSWORD, HOST, PORT
+ MySQL option files.

### Navigate to settings.py 
Add the following code
```python
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }
}
```

Next, let’s edit the config file so that it has your MySQL credentials. Use nano as sudo to edit the file and add the following information:

```bash
sudo nano /etc/mysql/my.cnf
```
Add the following lines

```bash
[client]
database = bit_game 
user = jacob     
password = vivian@123          
default-character-set = utf8
```

Once the file has been edited, we need to restart MySQL for the changes to take effect.

```bash
sudo systemctl daemon-reload
sudo systemctl restart mysql
```

## Test MySQL Connection to Application
```bash
python manage.py migrate
```
### Requirements
+ python-dev 
+ mysql-server 
+ libmysqlclient-de

# Visualization of the data

https://realpython.com/python-dash/#deploy-your-dash-application-to-heroku 
July 5th 2021
As you install heroku on raspberry pi you must also install node js as a must 

Heroku requires a graphical user interface to login hence i must install the graphical user interface of ubuntu
```python
$ sudo apt install lubuntu-desktop


```

# If i need to log in to the Heroku CLI without a browser.(This took two days to uncover)
```bash
heroku login -i
```

### How to make a bash script run in cron example
```bash
@reboot sleep 90  && /usr/bin/bash /home/ubuntu/.code/django_arduino/vivian/automate.sh
```
The line above , thats how you write a cron job at reboot ,give some time to fully boot 

# Automation
Here is used shell scripting 
## Requirements
+ Django
+ Arduino IDE
+ SQL
+ HTML
+ Python


# It took me one month and thirty days to finish the prototype July 6 2021
## References
How to Play Pool Table
https://www.gametablesonline.com/blog/how-to-play-pool-beginners-guide/

User management using Django
https://realpython.com/django-user-management/

Open ssh
https://help.ubuntu.com/community/SSH/OpenSSH/ConnectingTo

How-to-enable-disable-automatic-login-in-ubuntu
https://vitux.com/how-to-enable-disable-automatic-login-in-ubuntu/

Sending emails with python
https://realpython.com/python-send-email/#sending-a-plain-text-email

crontab at reboot
https://phoenixnap.com/kb/crontab-reboot

how-to-create-a-django-app-and-connect-it-to-a-mysql-database
https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database

how-to-deploy-your-app-to-heroku-from-raspberry-pi-
https://dev.to/heroku/how-to-deploy-your-app-to-heroku-from-raspberry-pi-162k\

how-to-install-node-js
https://gist.github.com/stonehippo/f4ef8446226101e8bed3e07a58ea512a

changing-username-and-hostname-on-ubuntu
https://www.hepeng.me/changing-username-and-hostname-on-ubuntu/

shell-script-submitting-a-password-after-a-prompt
https://daniel-ellis.medium.com/shell-script-submitting-a-password-after-a-prompt-690bcf144c0e


# django_arduino
