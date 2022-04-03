FROM python:3.10

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN ./create_env.sh

EXPOSE $PORT

CMD ["python", "app.py"]