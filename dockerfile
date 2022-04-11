FROM python:latest

WORKDIR /usr/src/cooler

COPY . /usr/src/cooler/

RUN pip3 install -U pip

RUN pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple

RUN pip3 config set install.trusted-host mirrors.aliyun.com

RUN pip3 install django==3.2

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

EXPOSE 8000

CMD [ "python", "manage.py", "runserver" ]