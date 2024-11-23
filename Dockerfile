FROM python:3.10.11
ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV TZ=Asia/Ho_Chi_Minh
RUN apt-get install -y tzdata
RUN echo $TZ > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata


RUN apt-get update && apt-get install -y
RUN apt-get install -y cron

WORKDIR /app
COPY . /app

RUN pip3 install --upgrade pip

RUN pip install requests
RUN pip install python-dotenv
RUN pip install elasticsearch
RUN pip install flask flask_cors

EXPOSE 5000

RUN chmod +x *.sh

CMD [ "./entrypoint.sh" ]
