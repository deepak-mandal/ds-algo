Running rabbit-mq ([localhost:5672](http://localhost:5672))
```bash
docker run --name rabbitTest -p 5672:5672 -d --hostname my-rabbit rabbitmq:3
```

Running neo4j ([localhost:7474](http://localhost:7474))
```bash
docker run --name neoTest -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/secret neo4j
```