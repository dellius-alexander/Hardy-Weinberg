FROM ubuntu:22.10
RUN apt-get update -y && apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .