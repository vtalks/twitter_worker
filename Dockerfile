FROM alpine:latest
MAINTAINER Raul Perez <repejota@gmail.com>

ADD requirements.txt /tmp/requirements.txt

RUN apk update && \
  apk upgrade && \
  apk add --no-cache gcc python3 py3-psycopg2 python3-dev musl-dev git && \
  pip3 install -r /tmp/requirements.txt && \
  rm -rf /var/cache/apk/*

ADD . /opt/twitter_worker
WORKDIR /opt/twitter_worker

CMD ["python3", "main.py"]
