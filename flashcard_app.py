import streamlit as st
import pandas as pd
from datetime import datetime

# Load existing words from CSV
def load_data():
    try:
        return pd.read_csv('vocabulary.csv')
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date Added", "Word", "Definition", "Example Sentence"])

# Save new word to CSV
def save_data(word, definition, example):
    data = load_data()
    new_entry = pd.DataFrame({"Date Added": [datetime.now().strftime("%Y-%m-%d")],
                              "Word": [word],
                              "Definition": [definition],
                              "Example Sentence": [example]})
    updated_data = pd.concat([data, new_entry], ignore_index=True)
    updated_data.to_csv('vocabulary.csv', index=False)

# Form to add new words
st.title("Flashcard App")
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose a feature", ["Add New Word", "Review Today's Words", "Review All Words"])

if option == "Add New Word":
    st.header("Add a New Word")
    
    # Form for user input
    with st.form("new_word_form"):
        word = st.text_input("Word")
        definition = st.text_input("Definition")
        example = st.text_input("Example Sentence")
        submit = st.form_submit_button("Add Word")
        
    if submit and word and definition and example:
        save_data(word, definition, example)
        st.success(f"'{word}' added to your vocabulary list!")



