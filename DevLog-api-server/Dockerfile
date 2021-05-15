FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /DevLog-api-server
WORKDIR /DevLog-api-server
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["manage.py"]