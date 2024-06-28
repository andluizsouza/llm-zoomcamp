# Module 1: Introduction
 
In this module, we will learn what LLM and RAG are and
implement a simple RAG pipeline to answer questions about 
the FAQ Documents from our Zoomcamp courses.

What we will do: 

* Index Zoomcamp FAQ documents
    * [DE Zoomcamp](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit)
    * [ML Zoomcamp](https://docs.google.com/document/d/1LpPanc33QJJ6BSsyxVg-pWNMplal84TdZtq10naIhD8/edit)
    * [MLOps Zoomcamp](https://docs.google.com/document/d/12TlBfhIiKtyBv8RnsoJR6F72bkPDGEvPOItJIxaEzE0/edit)
* Create a Q&A system for answering questions about these documents 

![](/images/llm-rag.png)

## 1.1 Introduction to LLM and RAG

YouTube Class: [1.1 - Introduction to LLM and RAG
](https://www.youtube.com/watch?v=Q75JgLEXMsM&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)

* LLM
* RAG
* RAG architecture
* Course outcome


## 1.2 Preparing the Environment

YouTube Class: [1.2 - Configuring Your Environment](https://www.youtube.com/watch?v=ozCpmkbJNJE&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R&index=2)

Create a `python3.9` virtual environment in the repository root (only once):

```bash
sudo apt-get install python3.9-venv
python3.9 -m venv venv
```

Activate this environment:

```
source venv/bin/activate
```

Install libraries:


```bash
make install
```

## 1.3 Retrieval and Search

YouTube Class: [1.3 - Retrieval and Search](https://www.youtube.com/watch?v=olvem333Bqo&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)

- Parse FAQ documents
    - [parse_faq.py](/01-introduction/parse_faq.py): function that reads a FAQ document from a Google Docs file and converts the questions and answers to a list of dict. 
    - [faq_database.json](/01-introduction/faq_database.json): output of the parse FAQ documents
- Indexing the documents
    - [minsearch.py](/01-introduction/minsearch.py): source code of the minimal search engine
- Performing the search


## 1.4 Generation with OpenAI

YouTube Class: [ 1.4 - Generating Answers with OpenAI GPT](https://www.youtube.com/watch?v=qz316T3U49Q&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R&index=4)

* Invoking OpenAI API
* Building the prompt
* Getting the answer

Bonus: [OpenAI API Alternatives
](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/01-intro/open-ai-alternatives.md)

_Personally, I have used Gemini API from Google because I don't have free credits to use the OpenAI API anymore and Google does not **yet** require an account with billing to use the Gemini API_. 

Moreover, Gemini 1.5 Flash model provides a free plan, that is very interesting for study cases.

***

**Gemini 1.5 Flash: free of charge (in June 2024)**

Rate Limits
- 15 RPM (requests per minute)
- 1 million TPM (tokens per minute)
- 1,500 RPD (requests per day)

Price (input)
- Free of charge

Price (output)
- Free of charge

Context caching
- Not applicable

Prompts/responses used to improve our products
- Yes

**References**
- https://ai.google.dev/pricing 
- https://aistudio.google.com/

API keys must be **secret** and **never exposed publicly**, so here it is used as an environment variable declared in `.env` file ignored by git.

## 1.5 Cleaned RAG flow

YouTube Class: [ 1.5 - The RAG Flow Cleaning and Modularizing Code](https://www.youtube.com/watch?v=vkTiVwwch6A&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R&index=6)

* Cleaning the code we wrote so far
* Making it modular

Code in Jupyter Notebook: [Intro_RAG.ipynb](/01-introduction/Intro_RAG.ipynb)

## 1.6 Searching with Elastic Search

YouTube Class: [1.6 - Search with Elastic Search](https://www.youtube.com/watch?v=1lgbR5wMvsI&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)

* Run ElasticSearch with Docker
* Index the documents
* Replace MinSearch with ElasticSearch

Running ElasticSearch:

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

Index settings:

```python
{
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "text": {"type": "text"},
            "section": {"type": "text"},
            "question": {"type": "text"},
            "course": {"type": "keyword"} 
        }
    }
}
```

Query:

```python
{
    "size": 5,
    "query": {
        "bool": {
            "must": {
                "multi_match": {
                    "query": query,
                    "fields": ["question^3", "text", "section"],
                    "type": "best_fields"
                }
            },
            "filter": {
                "term": {
                    "course": "data-engineering-zoomcamp"
                }
            }
        }
    }
}
```

We use `"type": "best_fields"`. You can read more about 
different types of `multi_match` search in [elastic-search.md](elastic-search.md).