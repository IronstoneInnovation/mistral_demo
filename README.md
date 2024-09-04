# Mistral Demo

A collection of simple yet fully functional chatbot apps to demonstrate how easy it is to use a locally-hosted Mistral LLM.  The architecture is just a straightforward Streamlit app that uses an Ollama server running locally to host the LLM and handle the requests from the app.  And thanks to Streamlit the entire project is pure Python - no HTML, CSS or javascript to deal with!

## Setting up

Assuming you have a suitable laptop with pyenv, pipenv and Ollama installed:

1. Clone this repository, create a Python environment and install packages:

```bash
$ git clone ...
$ cd mistral_demo
$ pipenv install
```

2. Install the Mistral-7B model on your computer:

```bash
$ ollama pull mistral
```

That's it!

## Running the demo

1. Start the local Ollama server.  This hosts the model in your computer's memory, enabling the demo apps to talk to it.  Open a Terminal and _leave it open when finished otherwise the server will terminate_:

```bash
$ ollama serve
```
"""

2. Open a new Terminal and start the streamlit server to serve the demo apps:

```bash
$ cd mistral_demo
$ streamlit run Home.py
```

The output will look something like this:

```bash
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
  Network URL: http://192.168.1.112:8501
```

Click on the Local URL to use the app.  Press CTRL-C or close the Terminal to shut the app down.
