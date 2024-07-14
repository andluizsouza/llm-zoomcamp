import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from min_search import Index


def create_index(database_path: str) -> Index:
    """
    Creates an index for the given database of documents.

    Parameters:
    database_path (str): The path to the database file.

    Returns:
    Index: The created index object.
    """

    with open(database_path, "rt") as f_in:
        docs_raw = json.load(f_in)

    documents = []

    for course_dict in docs_raw:
        for doc in course_dict["documents"]:
            doc["course"] = course_dict["course"]
            documents.append(doc)

    index = Index(
        text_fields=["question", "text", "section"], keyword_fields=["course"]
    )

    index.fit(documents)

    return index


def search(question: str, index: Index, filter_dict: dict = {}, num_results=5) -> list:
    """
    Search for relevant results based on the given question and course.

    Parameters:
    question (str): The question to search for.
    index (Index): The search index object.
    course (str): The course to filter the search results.
    num_results (int): The number of results to return. Default is 5.

    Returns:
    list: A list of search results.
    """

    boost = {"question": 3.0, "section": 0.5}

    results = index.search(
        query=question,
        filter_dict=filter_dict,
        boost_dict=boost,
        num_results=num_results,
    )

    return results


def create_model(env_file_path: str = ".env") -> genai.GenerativeModel:
    """
    Set up and configure the generative model.

    Args:
        env_file_path (str): Path to the environment file. Defaults to "../.env".

    Returns:
        genai.GenerativeModel: The configured generative model.
    """

    load_dotenv(env_file_path)
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY)

    generation_config = {
        "temperature": 0.1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 1024,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    return model


def build_prompt(query: str, search_results: list) -> str:
    """
    Build a prompt for generating an answer based on a given user query and search results.

    Args:
        query (str): The question/query for which the prompt is being built.
        search_results (list): A list of dictionaries containing search results.

    Returns:
        str: The generated prompt.

    """

    prompt_template = """
You're a course teaching assistant. Try answer the QUESTION using the the CONTEXT from the FAQ database.
If question is a greeting, answer with a kind greeting as well.
If question is about a specific course, use the facts from the CONTEXT to answer the QUESTION.
If question is general but about Data Science and Machine Learning topics, use your own knowledge to answer.
If question is out of the data/tecnology context, return *I am a course teaching assistant and your question is
out of the course context, so I can't help you. Please try again*.
QUESTION: {question}

CONTEXT: 
{context}

""".strip()

    context = ""

    for doc in search_results:
        context = (
            context
            + f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}\n\n"
        )

    prompt = prompt_template.format(question=query, context=context).strip()

    return prompt


def invoke_llm(prompt: str, model: genai.GenerativeModel, history: list = None) -> str:
    """
    Invokes the LLM (Language Model) to generate a response based on the given prompt.

    Parameters:
    prompt (str): The input prompt for the LLM.
    model (genai.GenerativeModel): The LLM model to be used for generating the response.
    history (list, optional): A list of previous chat messages as history. Defaults to None.

    Returns:
    str: The generated response from the LLM.
    """

    chat_session = model.start_chat(history=history)

    response = chat_session.send_message(prompt)

    return response.text


def run_rag(
    query: str, index: Index, model: genai.GenerativeModel, filter_dict: dict = {}
) -> str:
    """
    Runs the RAG (Retrieval-Augmented Generation) model to generate an answer based on the given query.

    Args:
        query (str): The query to search for.
        index (Index): The search index object.
        model (genai.GenerativeModel): The RAG model to use for generation.
        filter_dict (dict, optional): A dictionary of filters to apply during the search. Defaults to {}.

    Returns:
        str: The generated answer.

    """

    search_results = search(
        question=query, index=index, filter_dict=filter_dict, num_results=5
    )

    prompt = build_prompt(query, search_results)

    answer = invoke_llm(prompt, model)

    return answer
