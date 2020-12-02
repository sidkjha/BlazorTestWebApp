FROM ubuntu:18.04
MAINTAINER srijibb5991@gmail.com

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn3 -y

COPY . /opt/docker/flaskappforblazorcln/

WORKDIR /opt/docker/flaskappforblazorcln/

RUN pip3 install -r requirements.txt

CMD ["python3", "insertsampledata.py"]
CMD ["gunicorn3", "-b", "0.0.0.0:5001", "wsgi:app", "--workers=3"]
