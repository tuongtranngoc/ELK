FROM python:3.10.11
ENV DEBIAN_FRONTEND=noninteractive

#Install libs
RUN apt-get update && apt-get install -y

WORKDIR /app
COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install flask flask_cors
RUN pip install requests

EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
