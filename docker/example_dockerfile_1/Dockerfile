FROM ubuntu:24.04

RUN apt-get -y update && \
    apt-get -y install python3

COPY hello.py /opt/hello.py

CMD ["python3", "/opt/hello.py"]