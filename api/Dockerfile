FROM ubuntu:20.04

LABEL author="Martin Pena" author_email="martin.a.pena@vanderbilt.edu"

RUN apt-get update -y && \
    apt-get install -y python3-pip

COPY ./requirements.txt /app/requirements.txt



WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app/app.py" ]