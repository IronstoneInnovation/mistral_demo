import random
import streamlit as st
import ollama

# Title and description/instructions
st.image("dark-branding.png")
st.title("Simple Streaming Chat")
st.write(
    "This is a simple chatbot that talks to a locally-hosted Mistral model.  It does not send data over the internet, nor does it store data, refer to local or external files and databases."
)
st.write(
    "By streaming the response from the model, we can read the response as it is generated instead of waiting for the entire response before we can read it."
)


# Wrapper for parsing streamed Ollama output
def streamed_response():
    response = ollama.chat(
        model="mistral", messages=st.session_state.messages, stream=True
    )

    for chunk in response:
        yield chunk["message"]["content"]


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What's on your mind?"):

    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display model response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(streamed_response())

    # Add model response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
