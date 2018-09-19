FROM python:alpine

COPY requirements.txt /root/requirements.txt

RUN apk --update add --virtual build-dependencies \
                     libffi-dev openssl-dev build-base && \
    pip install -r /root/requirements.txt && \
    apk del build-dependencies && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/build

COPY src/ /app

CMD [ "python", "/app/main.py" ]
