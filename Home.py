import streamlit as st

st.set_page_config(page_title="Mistral Demo")

st.image("dark-branding.png")
st.write("# Local LLM Demo")
st.write("Well it started with Mistral, and then it grew...")
st.write(
    "A collection of simple yet fully functional chatbot apps to demonstrate how locally-hosted LLMs.  The architecture is just a straightforward Streamlit app that uses an Ollama server running locally to host the LLM and handle the requests from the app.  And thanks to Streamlit the entire project is pure Python - no HTML, CSS or javascript to deal with!"
)
st.write("⚡ Top Tip: Switch between different models and see which model works best.")
