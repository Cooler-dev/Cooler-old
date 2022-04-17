FROM python:latest

WORKDIR /usr/src/cooler

COPY . /usr/src/cooler/

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]