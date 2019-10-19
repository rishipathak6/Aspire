#!/bin/csh
#------------------------------------------------------------------------------#
# deploy.csh                                                                   #
#------------------------------------------------------------------------------#
# By: Bartlomiej Mika
# Date: April, 27th, 2015
#
# Description:
# This script will load up the django virtual environment instance
# and start the web-server.
#
# Prerequsites:
# (1) Running on FreeBSD OS
# (2) Running in user called 'freebsd'
# (3) aspire dir: /usr/home/freebsd/py-aspire
#
#----------------#
# HOWTO: Setup:  #
#----------------#
# (1) Give permission
# $ chmod u+x /usr/home/freebsd/py-aspire/scripts/deploy.csh
#
# (1) Run command:
# $ /usr/home/freebsd/py-aspire/scripts/deploy.csh

# Clear all text on the screen
clear;

# Turn on virtual environment
source /usr/home/freebsd/py-aspire/env/bin/activate.csh

# Bugfix
ln -s /usr/home/freebsd/py-aspire/env/lib/python3.4/site-packages/django/contrib/admin/static/admin /usr/home/freebsd/py-aspire/aspire_project/static/admin

# Run command
cd /usr/home/freebsd/py-aspire/aspire_project
gunicorn -c gunicorn_config.py aspire_project.wsgi
