#!/bin/bash --login

printenv | grep -v "no_proxy" >> /etc/environment
source /etc/environment

python app.py &

echo "Initialize out.log file" > /app/out.log
echo "*/2 * * * *   root  cd /app && (/app/data_manager.sh) >> /app/out.log 2>&1" >> /etc/crontab

service cron reload
service cron restart
crontab /etc/crontab
crontab -l

echo "tail -f /app/out.log"
tail -f /app/out.log