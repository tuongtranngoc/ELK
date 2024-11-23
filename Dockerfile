FROM python:3.10.11
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y

WORKDIR /app
COPY . /app

RUN pip3 install --upgrade pip

RUN pip install requests
RUN pip install elasticsearch
RUN pip3 install flask flask_cors

EXPOSE 5000

CMD ["python", "app.py"]
