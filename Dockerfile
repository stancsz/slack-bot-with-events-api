# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py .
COPY plugins/slackbot_api_handler .
COPY plugins/slackbot_intents_and_subroutines .
COPY plugins/slackbot_intents_and_subroutines/intents .
COPY plugins/slackbot_intents_and_subroutines/subroutines .

ENV FLASK_ENV="development"

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]