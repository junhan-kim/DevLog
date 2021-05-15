FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential
RUN apt-get install -y python3-psycopg2
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

ENV DATABASE_URL postgres://postgres:940416@localhost:5432/devlog
ENV SECRET_KEY 'secret'
ENV BOILERPLATE_ENV dev

COPY . /DevLog-api-server
WORKDIR /DevLog-api-server
RUN pip install -r requirements.txt
RUN python manage.py db init
RUN python manage.py db migrate --message 'initial database migration'
RUN python manage.py db upgrade

ENTRYPOINT [ "python" ]
CMD ["manage.py", "run"]
