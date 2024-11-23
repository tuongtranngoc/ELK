#!/bin/bash --login

printenv | grep -v "no_proxy" >> /etc/environment
source /etc/environment

python data_manager.py