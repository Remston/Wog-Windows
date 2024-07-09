FROM python:slim

WORKDIR /app

COPY  . /app

EXPOSE 80

ENV name WOG

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]