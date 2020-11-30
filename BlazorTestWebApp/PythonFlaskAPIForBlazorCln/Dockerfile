FROM python:3.7.9

COPY . /opt/docker

WORKDIR /opt/docker

RUN pip install -r requirements.txt

EXPOSE 5001

ENV FLASK_APP /opt/docker/runserver.py

CMD flask run --host=0.0.0.0 --port=5001 
