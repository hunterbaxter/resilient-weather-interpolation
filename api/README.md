# API Documentation

## Running the API on a machine

There are a few things which are needed to run the flask API.
Python3, Kafka, numpy, scipy, apscheduler

Have to add tzlocal==2.1 manually to requirements.txt

## Docker Image Repo:

### Pushing Docker Image

```
docker build -t <your_image_name>:latest .
```

```
docker tag <your_image_name>:latest alexpena9291/cloud_computing:<your_image_name>
```

```
docker push alexpena9291/cloud_computing:<your_image_name>
```

or just double-click the 'docker_stuff.command' file and it will run this for
you!

P.S. To do this you need to be signed into my (Alex's) docker account.

### Pulling Docker Image

```
docker pull alexpena9291/cloud_computing:weather_api
```

```
docker run -d -p 8080:8080 alexpena9291/cloud_computing:weather_api
```

## Endpoint(s) Avaliable

> **/kepler/data** will return a GeoJSON object.
