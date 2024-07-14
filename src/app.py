import streamlit as st
from min_rag import create_index, create_model, run_rag

index = create_index(database_path="src/faq_database.json")
model = create_model(env_file_path=".env")


def main():
    """
    Main function that runs the RAG Chatbot application.
    """

    st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")

    st.title("💬 Chatbot: RAG Invocation")

    courses = [
        "General",
        "Data Engineering Zoomcamp",
        "Machine Learning Zoomcamp",
        "MLOps Zoomcamp",
    ]
    option = st.sidebar.selectbox(label="Select the course context:", options=courses)
    option = option.lower().replace(" ", "-")
    if option == "general":
        filter_dict = {}
    else:
        filter_dict = {"course": option}

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "How can I help you?"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = run_rag(
            query=prompt, index=index, model=model, filter_dict=filter_dict
        )
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

    st.sidebar.write("***")
    st.sidebar.image("images/llm-zoomcamp.jpg")
    st.sidebar.write(
        "*This is a chatbot that uses the Retrieval-Augmented Generation (RAG) model to answer questions based on the Zoomcamp FAQ database.*"
    )
    st.sidebar.write("Developed by [Anderson Souza](https://github.com/andluizsouza)")


if __name__ == "__main__":
    main()
