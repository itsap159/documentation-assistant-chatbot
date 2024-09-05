from backend.rag import get_response
import streamlit as st
from streamlit_chat import message
import time
from typing import Set
st.set_page_config(page_title="Langchain Documentation Assistant", layout="wide")
st.header("Langchain Documentation Assistant")
if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []
if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "Sources: \n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i + 1}. {source}\n"  # Corrected f-string formatting
    return sources_string



prompt = st.text_input("Prompt", placeholder="Enter yuor prompt here.....")


if prompt:
    with st.spinner("Generating response....."):
        out = get_response(prompt,
                           chat_history = st.session_state['chat_history'])
        sources = set([all.metadata["source"] for all in out['source_documents']])
        final_response = f"{out['result']} \n\n\n {create_sources_string(sources)}"
        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(final_response)
        st.session_state['chat_history'].append(("human", prompt))
        st.session_state['chat_history'].append(("ai", out['result']))


if st.session_state["chat_answers_history"]:
    for ques, ans in zip(reversed(st.session_state["user_prompt_history"]), reversed(st.session_state["chat_answers_history"])):
        message(ques, is_user=True)
        message(ans)


st.markdown("""
<style>
.css-1d391kg p {
    word-wrap: break-word;
}
</style>
""", unsafe_allow_html=True)
