# Manual Instructions
for automation, see [infrastructure directory](../infrastructure)

Key for weatherbit (just free-tier test key):
"0e8aeccfa150491880a30ffb53a3e4ba"

## Prerequisites

- Kafka server on ip
- Either running from docker image,
or with pip packages in requirements.txt installed ```pip install -r requirements.txt```

## Native

```
python3 main_retriever.py \
    --kafka_ip 18.118.248.88 \
    -a 0e8aeccfa150491880a30ffb53a3e4ba \
    --interval 1
```

## With Docker

- Build Docker Image

```
docker build -f dockerfile_retriever -t retriever .
```

- Start Docker Container

```
docker run -itd --name ret retriever
```

- Run retriever code

```
docker exec -it ret python3 /main_retriever.py \
    --kafka_ip 18.118.248.88 \
    -a 0e8aeccfa150491880a30ffb53a3e4ba \
    --interval 1
```
