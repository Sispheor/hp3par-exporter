# docker build --rm -t hp3par-exporter .
# docker run -p 8080:8080 -v $PWD/hp3par_config.yml:/hp3par_config.yml hp3par-exporter

FROM python:3.6-slim
RUN apt-get update && apt-get install -y \
    build-essential
ADD . /tmp/hp3par_exporter
RUN cd /tmp/hp3par_exporter && python setup.py install
ENTRYPOINT ["hp3par-exporter"]
EXPOSE 8080
