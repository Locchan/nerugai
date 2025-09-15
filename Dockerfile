FROM python:3.12-alpine

WORKDIR /

COPY nerugai.py .
RUN pip install python-telegram-bot

RUN ln -s /usr/share/zoneinfo/Europe/Minsk /etc/localtime

RUN echo "${VERSION}" > /version

ENTRYPOINT [ "/usr/bin/env", "python3",  "/nerugai.py"]
