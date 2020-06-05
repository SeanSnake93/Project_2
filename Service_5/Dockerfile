ARG PYTHON_VERSION=3.7

FROM python:latest

RUN mkdir /opt/services/

COPY . /opt/services/

WORKDIR /opt/services/

RUN pip3 install -r requirements.txt

EXPOSE 5004

ENTRYPOINT ["/usr/local/bin/python3", "app.py"]

