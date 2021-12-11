# Manual Instructions

"0e8aeccfa150491880a30ffb53a3e4ba",


## Prerequisites

- Kafka on instance

## Steps

- Build Docker Image

```
docker build -f dockerfile_retriever -t retriever .
```

- Start Docker Container

```
docker run -itd --name r00 retriever
```

- Run retriever code

```
docker exec -it r00 python3 /main_retriever.py \
    --kafka_ip 18.118.248.88 \
    -a weatherbit_key \
    --interval 1
```

```
python3 main_retriever.py \
    --kafka_ip 18.118.248.88 \
    -a 0e8aeccfa150491880a30ffb53a3e4ba \
    --interval 1
```
