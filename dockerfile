FROM python:latest

WORKDIR /usr/src/cooler

COPY . /usr/src/cooler/

RUN pip3 install -r requirements.txt

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]