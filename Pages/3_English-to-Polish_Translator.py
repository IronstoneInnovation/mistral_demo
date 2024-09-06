import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

st.set_page_config(page_title="English-to-Polish Translator 🏴󠁧󠁢󠁥󠁮󠁧󠁿🇵🇱")

# Title and description/instructions
st.image("dark-branding.png")
st.title("English-to-Polish Translator 🏴󠁧󠁢󠁥󠁮󠁧󠁿🇵🇱")
st.write(
    "Siemanko! Translate documents from English to Polish this simple app. No need to worry about devious Silicon Valley cringelords stealing your confidential documents - nothing leaves your laptop."
)

# Select model
model_name = st.selectbox(
    "Select a model (wybierz model):",
    (
        "mistral",
        "llama3.1:8b",
    ),
)

# Input form with submit button
with st.form(key="input_form"):
    text = st.text_area(
        label="Enter the text for translation (wprowadź tekst do przetłumaczenia):"
    )
    submitted = st.form_submit_button(label="Submit")

# The prompt template
# (Note that we would normally need to be more careful about formatting prompts
# particularly with llama3 but for this demo it's better to keep things simple.)
template = f"""
Reply ONLY with the document in Polish.

Document:
{text}

Po Polsku:
"""

if submitted:
    # Use LangChain to populate a prompt and get a response from Mistral
    prompt = ChatPromptTemplate.from_template(template)
    model = OllamaLLM(model=model_name)
    chain = prompt | model
    response = chain.invoke({"text": text})
    st.markdown("## Translation")
    st.write(response)
