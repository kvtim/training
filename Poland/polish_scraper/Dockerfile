# FROM python:3.10 AS py3
FROM openjdk:8-slim-buster

# COPY --from=python:3.10 / /

RUN apt-get update && apt-get install -y python3 python3-pip libpq-dev

WORKDIR /app

COPY . /app

RUN ./create_env.sh

EXPOSE 5000

ENTRYPOINT [ "python3" ]
CMD [ "run.py"]
