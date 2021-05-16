FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential
RUN apt-get install -y python3-psycopg2
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

COPY . /DevLog-api-server
WORKDIR /DevLog-api-server
ENV DATABASE_URL postgresql://postgres:940416@db/devlog
ENV SECRET_KEY secret
ENV BOILERPLATE_ENV dev
RUN pip install -r requirements.txt

ENTRYPOINT ["./docker-entrypoint.sh"]
