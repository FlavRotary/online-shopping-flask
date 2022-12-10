FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update && apt-get -y install \
    python3 \
    build-essential

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --src /usr/local/src

ADD . . 

ENV FLASK_APP=product
EXPOSE 5000
ENTRYPOINT ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--reload"]