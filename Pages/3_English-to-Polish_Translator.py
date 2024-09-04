import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Title and description/instructions
st.image("dark-branding.png")
st.title("English-to-Polish Translator 🏴󠁧󠁢󠁥󠁮󠁧󠁿🇵🇱")
st.write(
    "Siemanko! Translate documents from English to Polish this simple app. No need to worry about Silicon Valley copelords stealing your confidential documents - nothing leaves your laptop."
)

# Input form with submit button
with st.form(key="input_form"):
    text = st.text_area(
        label="Enter the text for translation (Wprowadź tekst do przetłumaczenia):"
    )
    submitted = st.form_submit_button(label="Submit")

# The prompt template
template = f"""
Reply ONLY with the document in Polish.

Document:
{text}

Po Polsku:
"""

if submitted:
    # Use LangChain to populate a prompt and get a response from Mistral
    prompt = ChatPromptTemplate.from_template(template)
    model = OllamaLLM(model="mistral")
    chain = prompt | model
    response = chain.invoke({"text": text})
    st.markdown("## Translation")
    st.write(response)
