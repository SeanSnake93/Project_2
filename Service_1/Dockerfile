FROM python:latest

RUN mkdir /opt/services/

COPY . /opt/services/

WORKDIR /opt/services/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]