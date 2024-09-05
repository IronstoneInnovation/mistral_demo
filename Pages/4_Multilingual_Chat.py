# Now we use LangChain to handle the message history as well.  This includes trimming the older messages.

from operator import itemgetter
import streamlit as st
from langchain_community.chat_models import (
    ChatOllama,
)  # Wow, ok see https://github.com/langchain-ai/langchain/issues/22060#issuecomment-2154205994
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    trim_messages,
)  # BTW: trim_messages also needs transformers installed!
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough


# Title and description/instructions
st.image("dark-branding.png")
st.title("Multilingual Chat")
st.write(
    "This is a more production-ready chatbot that supports multiple languages.  You can write to it in any language, but it will always try to respond in the selected Assistant Language."
)
st.write(
    "Under the hood it uses LangChain to manage the prompting, chat history and responses to and from the model, which is still hosted locally."
)
st.write(
    "As always, it does not send data over the internet, nor does it store data or refer to local or external files and databases...but one of the language options is NSFW so be careful!"
)

# Select model
model_name = st.selectbox(
    "Select a model:",
    (
        "mistral",
        "llama3.1:8b",
    ),
)

# Select assistant language
language = st.selectbox(
    "Assistant Language",
    (
        "English",
        "Polish",
        "German",
        "French",
        "Spanish",
        "Hollywood Pirate Talk",
        "the slightly sweary style of Lemmy Kilmister (NSFW!)",
    ),
)

# Initialize message history, chat history trimmer, model and runnable
if "store" not in st.session_state:
    st.session_state.store = {}


config = {"configurable": {"session_id": "abc2"}}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = InMemoryChatMessageHistory()
    return st.session_state.store[session_id]


model = ChatOllama(model=model_name)

trimmer = trim_messages(
    max_tokens=8192,  # Current context window of Mistral-7B
    strategy="last",
    token_counter=model,
    include_system=True,
    allow_partial=False,
    start_on="human",
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability in {language}.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = (
    RunnablePassthrough.assign(messages=itemgetter("messages") | trimmer)
    | prompt
    | model
)

with_message_history = RunnableWithMessageHistory(
    chain, get_session_history, input_messages_key="messages"
)


# Wrapper for parsing streamed model response
def streamed_response(prompt, language):
    for r in with_message_history.stream(
        {
            "messages": [HumanMessage(content=prompt)],
            "language": language,
        },
        config=config,
    ):
        yield r.content


# Display chat messages from history on app rerun
history = get_session_history(config["configurable"]["session_id"])
for message in history.messages:
    if isinstance(message, AIMessage):
        role = "ai"
    else:
        role = "human"
    with st.chat_message(role):
        st.markdown(message.content)

# React to user input
if prompt := st.chat_input("What's on your mind?"):

    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    # Display model response in chat message container
    with st.chat_message("ai"):
        st.write_stream(streamed_response(prompt, language))
