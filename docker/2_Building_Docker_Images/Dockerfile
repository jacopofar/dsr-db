FROM ubuntu:20.04

RUN apt-get -y update && \
	apt-get -y install wget

COPY hello.sh /opt/hello.sh

RUN chmod +x /opt/hello.sh

CMD ["bash", "/opt/hello.sh"]

