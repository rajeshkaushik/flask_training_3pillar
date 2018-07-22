FROM python:3.6.6-slim-stretch

RUN apt-get update && \
    apt-get install -y curl apt-transport-https &&\
    curl http://packages.microsoft.com/config/debian/9/prod.list > \
    /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update \
    && apt-get install -y \
        build-essential && \
        apt-get install -y curl unixodbc-dev \
        && ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17


RUN mkdir -p /appl/flask_training_3pillar/logs
RUN mkdir -p /var/log/gunicorn

COPY . /appl/flask_training_3pillar/

WORKDIR /appl/flask_training_3pillar/demo
RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]
