FROM ubuntu:22.04

WORKDIR /mydir

COPY script.sh .

RUN apt-get update && \
  apt-get upgrade && \
  apt-get install -y curl

RUN chmod +x script.sh

ENTRYPOINT ["./script.sh"]
