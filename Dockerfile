FROM python:3.10-alpine3.19

ADD . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "flask" , "run" , "--debug" , "-h", "0.0.0.0", "-p", "5000"]

