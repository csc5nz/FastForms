
# Installation Instructions

## Table of Contents
1. [Overview](#overview)  
2. [Assumptions](#assumptions)  
3. [Source Code Download](#source-code-download)  
4. [Virtual Environment Setup and Package Installation](#virtual-environment-setup-and-package-installation)  
5. [Database Creation and Setup](#database-creation-and-setup) 
5. [Django Settings File Update](#django-settings-file-update)  
6. [Data Migration and Server Startup](#data-migration-and-server-startup)  

## Overview


## Assumptions
- The server has Apache installed
- The server has MySQL installed 
- phpMyAdmin is installed (or they can install it) -- this is a single package on Ubuntu
-    - `sudo apt-get install phpmyadmin`
- That they are installing the software system (not the LAMP stack) from scratch (i.e., creating the database, etc.)
- The user installing the system has access to the github repository with the source code.


Throughout the Installation Instructions, username, password, and hostname will be referred to as USERNAME, PASSWORD, and HOSTNAME. Wherever these appear, substitute in your username and password and your server hostname.
  

## Source Code Download

- Run: `git clone https://github.com/csc5nz/FastForms`




## Virtual Environment Setup and Package Installation
sudo apt-get install python-virtualenv
If prompted, answer yes to using more disk space
- cd into the main directory. This will probably be `cd FastForm/
- Create a virtual environment using `virtualenv -p /usr/bin/python3 env`
- Next, run this command to activate the virtualenv `source env/bin/activate`
- If you do not already have pip, install it using `sudo apt-get install python3-pip`
- Finally, install all dependent packages. to install the required packages is `pip3 install -r requirements.txt`

## Database Creation and Setup 

If database and database user have not been created,
- Start mysql and login as root by running: 
- `mysql -u root -p`
- In mysql, create database with name ‘fastform’ by running:
- `Create database ‘fastform’;`
- In mysql, create a user named ‘username’’ with password ‘password’ and grant all privileges to this user by running: 
- `GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password';`


## Django Settings File Update
Create a file “secrets.py” in the same directory as settings.py and add the following lines of code
- secrete_key = 'o3uo3dceyst)tvgn=lxqezl@&casd3)4buxxt97wh$rx^y*nq4'
- database_engine = "django.db.backends.mysql"
- database_host = "127.0.0.1"
- database_name = "fastform"
- database_user = "fastform"
- database_password = "frog1234"
- #static_root = ""
- #static_url = ""




## Data Migration and Server Startup

From the directory containing manage.py run the following commands:
- python manage.py collectstatic
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
