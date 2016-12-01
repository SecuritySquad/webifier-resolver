FROM debian:latest

COPY test.py /tmp/

RUN apt-get -y update && apt-get install -y ca-certificates python

CMD python /tmp/test.py $ID $URL