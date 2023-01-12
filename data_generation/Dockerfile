FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

CMD ["tail", "-f",  "/dev/null"]