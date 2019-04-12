FROM ubuntu:16.04

MAINTAINER Yi Fu

RUN apt-get update -y && apt-get install -y python-pip python-dev

COPY ./requirements.txt /src/requirements.txt
WORKDIR /src

RUN pip install -r requirements.txt

COPY sample_table_docker /src
COPY init_sh/init.sh /usr/local/bin/init.sh
RUN chmod +x /usr/local/bin/init.sh


CMD ["/usr/local/bin/init.sh"]

