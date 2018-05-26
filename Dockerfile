FROM python:3.6-alpine

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/
RUN apk update && \
    apk add --virtual .build-deps gcc musl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk --purge del .build-deps

COPY api wsgi.py docs /app/
WORKDIR /app

EXPOSE 8000/tcp
ENTRYPOINT ["gunicorn",  "-w",  "4", "-b",  "0.0.0.0:8000", "wsgi:app"]
