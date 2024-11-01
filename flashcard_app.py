import streamlit as st
import pandas as pd
import random


# Load flashcards data from the Excel file
file_path = 'new_word.xlsx'
flashcards_df = pd.read_excel(file_path)
flashcards = flashcards_df.to_dict(orient='records')


# Function to pick a new random flashcard
def new_flashcard():
    if flashcards:  # Ensure flashcards list is not empty
        st.session_state.current_flashcard = random.choice(flashcards)


# Initialize session state to store the flashcard
if 'current_flashcard' not in st.session_state:
    new_flashcard()  # Set a flashcard at the start


# Streamlit app title
st.title("---------------")


# Get the current flashcard from session state
if 'current_flashcard' in st.session_state:
    card = st.session_state.current_flashcard

    # Display the flashcard information
    st.subheader(f"Word: {card['Word']}")
    st.text(f"Pronunciation: {card['Pronounce']}")
    st.text(f"Kind of Word: {card['Kind of word']}")

    # Button to reveal the meaning
    if st.button("Show Meaning"):
        st.write(f"**Meaning:** {card['Meaning']}")
        st.write(f"**Common collocation:** {card['common collocation']}")
        st.write(f"**Synonym:** {card['Synonym']}")
        st.write(f"**Example:** {card['Example']}")
else:
    st.write("No flashcard available.")


# Button to load a new flashcard
if st.button("Next Flashcard"):
    new_flashcard()
    st.rerun()
