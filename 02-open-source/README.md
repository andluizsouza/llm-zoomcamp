# 2. Open-Source LLMs

In the previous module, we used Gemini 1.5 Flash via Google API. It's a very convenient way to use an LLM, but you have to pay for the usage, and you don't have control over the model you get to use.

In this module, we'll look at using open-source LLMs instead.

## 2.1 Introduction

YouTube Class: [2.1 - Introduction to Open-Source](https://www.youtube.com/watch?v=ATchkIRsH4g&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)

* Open-Source LLMs
* Replacing the LLM box in the RAG flow

## 2.2 Using a GPU in Saturn Cloud

YouTube Class: [2.2 - Using SaturnCloud for GPU Notebooks](https://www.youtube.com/watch?v=E0cAqBWfJYY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R&index=9)

* Registering in Saturn Cloud
* Configuring secrets and git
* Creating an instance with a GPU

Bonus: [Using Google Colab for GPU Notebooks](https://www.loom.com/share/591f39e4e231486bbfc3fbd316ec03c5)
> *This is my personal choice!*

## 2.3 Model: Google FLAN-T5

YouTube Class: [2.3 - HuggingFace and Google FLAN T5](https://www.youtube.com/watch?v=a86iTyxnFE4&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R&index=10)

* HuggingFace Model: `google/flan-t5-xl`
* Jupyter Notebook: [Model_FlanT5.ipynb](/02-open-source/Model_FlanT5.ipynb)
* References:
    * [huggingface.co/google/flan-t5-xl](https://huggingface.co/google/flan-t5-xl) 
    * [huggingface.co/docs/transformers/en/model_doc/flan-t5](https://huggingface.co/docs/transformers/en/model_doc/flan-t5)


## 2.4 More models

* Phi 3 Mini
    *  YouTube Class: [2. 4 - Phi 3 Mini](https://www.youtube.com/watch?v=8KH6AS2PqWk&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)
    * HuggingFace Model: `microsoft/Phi-3-mini-128k-instruct`
    * Reference: [huggingface.co/microsoft/Phi-3-mini-128k-instruct](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct)
* Mistral-7B and HuggingFace Hub Authentication
    * YouTube Class: [2.5 - Mistral-7B](https://www.youtube.com/watch?v=TdVEOzSoUCs&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R&index=12)
    * HuggingFace Model:  `mistralai/Mistral-7B-v0.1`
    * Reference: [huggingface.co/mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)
* Exploring Open-Source Models
    * YouTube Class: [2.6 - Exploring Open Source LLMs](https://www.youtube.com/watch?v=GzPV_HTmCkc&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R&index=13)
    * [HF: Generation with LLMs](https://huggingface.co/docs/transformers/en/llm_tutorial)
    * [HF: Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
    * [HF: LLM-Perf Leaderboard](https://huggingface.co/spaces/optimum/llm-perf-leaderboard)

## 2.5 Ollama - Running LLMs on a CPU

YouTube Class: [2.7 - Running LLMs Locally without a GPU with Ollama](https://www.youtube.com/watch?v=PVpBGs_iSjY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)

Install and start `Ollama`:
```
curl -fsSL https://ollama.com/install.sh | sh
ollama start
```

Pull (only once) and run locally a model:
```
ollama pull phi3
ollama run phi3
```
then a chat with the model will be opened from the command line interface.

* [Intro_RAG.ipynb](/02-open-source/Intro_RAG.ipynb): RAG system using `phi3` local model
    * Pros: open-source models and codes, totally free
    * Cons: very slow running and probably not scalable

* [Ollama model libray](https://github.com/ollama/ollama?tab=readme-ov-file#model-library)

* [GitHub: Ollama](https://github.com/ollama/ollama)

