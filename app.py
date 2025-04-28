import streamlit as st
from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Streamlit app
st.title("Text Georges Summarizer ✨")

# Text input from user
text_input = st.text_area("Paste your text below:")

# Button to trigger summarization
if st.button("Summarize"):
    if text_input.strip() != "":
        summary = summarizer(text_input, max_length=50, min_length=25, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please paste some text before clicking Summarize!")
