FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

ENV DATABASE_URL = postgres://postgres:940416@localhost:5432/devlog
ENV SECRET_KEY = '940416'
ENV BOILERPLATE_ENV dev

COPY . /DevLog-api-server
WORKDIR /DevLog-api-server
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["manage.py", "run"]