import streamlit as st
import ollama

# Title and description/instructions
st.image("dark-branding.png")
st.title("Simple Chat")
st.write(
    "This is a simple chatbot that talks to a locally-hosted Mistral model.  It does not send data over the internet, nor does it store data, refer to local or external files and databases."
)

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

    # Get response from model
    response = ollama.chat(
        model="mistral",
        messages=st.session_state.messages,
    )

    # Display model response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response["message"]["content"])

    # Add model response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response["message"]["content"]}
    )
