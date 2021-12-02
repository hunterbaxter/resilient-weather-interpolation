# Kafka

docker image
```
docker pull bitnami/kafka:latest
docker pull bitnami/zookeeper:latest
```

```
docker run -d --name kafka-server \
    --network app-tier \
    -e ALLOW_PLAINTEXT_LISTENER=yes \
    -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 \
    -e KAFKA_CFG_AUTO_CREATE_TOPICS_ENABLE=true \
    -e KAFKA_TLS_CLIENT_AUTH=none \
    bitnami/kafka:latest
```

# Resources
[bitnami images](https://hub.docker.com/r/bitnami/kafka/)
