FROM python:3.9
MAINTAINER "rinatlucke@gmail.com"

ENV PYTHONPATH=/app

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD bash app/prepare.sh
