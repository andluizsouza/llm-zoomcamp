# 3. Vector Search

## 3.1 Intro to Vector Search

YouTube Class: [3.1 - Introduction to Vector Search](https://www.youtube.com/watch?v=C5AWdL3kg1Q&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)

Slides: [references/Intro_to_VectorDB.pdf](/03-vector-search/references/Intro_to_VectorDB.pdf)

- [What are vector embeddings?](https://www.elastic.co/what-is/vector-embedding)
- [What is a vector database?](https://www.elastic.co/what-is/vector-database)

![](/03-vector-search/references/vector-search-diagram.png)


## 3.2 Semantic Search

YouTube Class: [3.2 - Semantic Search with ElasticSearch](https://www.youtube.com/watch?v=ptByfB_YcEg&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R&index=18)

Running ElasticSearch locally:

```bash
docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```
Notebook: [Semantic_Search.ipynb](/03-vector-search/Semantic_Search.ipynb)

- [Text similarity search with vector fields](https://www.elastic.co/search-labs/blog/text-similarity-search-with-vectors-in-elasticsearch)
- [SBERT: pretrained models](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html)