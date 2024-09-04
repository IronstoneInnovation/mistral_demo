import streamlit as st

st.set_page_config(page_title="Mistral Demo")

st.image("dark-branding.png")
st.write("# Mistral Demo")
st.write(
    "A collection of simple yet fully functional chatbot apps to demonstrate how easy it is to use a locally-hosted Mistral LLM.  The architecture is just a straightforward Streamlit app that uses an Ollama server running locally to host the LLM and handle the requests from the app.  And thanks to Streamlit the entire project is pure Python - no HTML, CSS or javascript to deal with!"
)
st.image("architecture.png")
st.write("## Setting up")
st.write("Assuming you have a suitable laptop with pyenv, pipenv and Ollama installed:")
st.write("1. Clone this repository, create a Python environment and install packages:")

st.markdown(
    """
    ```bash
    $ git clone ...
    $ cd mistral_demo
    $ pipenv install
    ```
    """
)
st.write("2. Install the Mistral-7B model on your computer:")
st.markdown(
    """
    ```bash
    $ ollama pull mistral
    ```
    """
)
st.write("That's it!")
st.write("## Running the demo")
st.write(
    "1. Start the local Ollama server.  This hosts the model in your computer's memory, enabling the demo apps to talk to it.  Open a Terminal and _leave it open when finished otherwise the server will terminate_:"
)
st.markdown(
    """
    ```bash
    $ ollama serve
    ```
    """
)
st.write(
    "2. Open a new Terminal and start the streamlit server to serve the demo apps:"
)
st.markdown(
    """
    ```bash
    $ cd mistral_demo
    $ streamlit run Home.py
    ```
    """
)
st.write("The output will look something like this:")
st.markdown(
    """
    ```bash
      You can now view your Streamlit app in your browser.

      Local URL: http://localhost:8501
      Network URL: http://192.168.1.112:8501
    ```
    """
)
st.write(
    "Click on the Local URL to use the app.  Press CTRL-C or close the Terminal to shut the app down."
)
