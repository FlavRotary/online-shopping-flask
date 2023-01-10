FROM python:3.11.1-slim

RUN apt-get clean \
    && apt-get -y update && apt-get -y install \
    python3 \
    build-essential

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt --src /usr/local/src

COPY /src/newsletter .

ENV FLASK_APP=/app/newsletter.py
EXPOSE 5000
ENTRYPOINT ["python3", "-m" , "flask", "run"]