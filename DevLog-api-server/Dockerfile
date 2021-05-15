FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential

COPY . /DevLog-api-server
WORKDIR /DevLog-api-server
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["manage.py"]