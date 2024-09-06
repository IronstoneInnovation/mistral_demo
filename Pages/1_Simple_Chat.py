import streamlit as st
import ollama

st.set_page_config(page_title="Simple Chat")

# Title and description/instructions
st.image("dark-branding.png")
st.title("Simple Chat")
st.write(
    "This is a simple chatbot that talks to a locally-hosted model.  It does not send data over the internet, nor does it store data or refer to local or external files and databases."
)

# Select model
model_name = st.selectbox(
    "Select a model:",
    (
        "mistral",
        "llama3.1:8b",
    ),
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
    # (Note that we would normally need to be more careful about formatting prompts
    # particularly with llama3 but for this demo it's better to keep things simple.)
    st.chat_message("user").markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from model
    response = ollama.chat(
        model=model_name,
        messages=st.session_state.messages,
    )

    # Display model response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response["message"]["content"])

    # Add model response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response["message"]["content"]}
    )
