FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update && apt-get -y install \
    python3 \
    build-essential

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt --src /usr/local/src

COPY . /app

ENV FLASK_APP=/app/newsletter.py
EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--reload"]
#CMD [ "python3", "/app/newsletter.py" ]