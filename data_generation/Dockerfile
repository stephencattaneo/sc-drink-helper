FROM python

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

CMD ["tail", "-f",  "/dev/null"]