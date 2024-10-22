import streamlit as st
import pandas as pd
import random
import openpyxl  # Ensure this library is installed for writing to Excel

# Load flashcards data from the Excel file
file_path = 'new_word.xlsx'
flashcards_df = pd.read_excel(file_path)
flashcards = flashcards_df.to_dict(orient='records')


# Function to pick a new random flashcard
def new_flashcard():
    if flashcards:  # Ensure flashcards list is not empty
        st.session_state.current_flashcard = random.choice(flashcards)


# Function to add a new flashcard
def add_new_flashcard(word, pronounce, kind, meaning, collocation, synonym, example):
    new_entry = {
        'Word': word,
        'Pronounce': pronounce,
        'Kind of word': kind,
        'Meaning': meaning,
        'common collocation': collocation,
        'Synonym': synonym,
        'Example': example
    }
    flashcards.append(new_entry)  # Add to flashcards list
    # Append the new word to the DataFrame
    new_flashcard_df = pd.DataFrame([new_entry])
    global flashcards_df  # Access the global variable
    flashcards_df = pd.concat([flashcards_df, new_flashcard_df], ignore_index=True)
    # Save the updated DataFrame back to the Excel file
    flashcards_df.to_excel(file_path, index=False)


# Initialize session state to store the flashcard
if 'current_flashcard' not in st.session_state:
    new_flashcard()  # Set a flashcard at the start


# Streamlit app title
st.title("Flashcard App")


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


# Add a form to input new flashcard data
st.subheader("Add a New Flashcard")
with st.form("new_flashcard_form"):
    new_word = st.text_input("Word")
    new_pronounce = st.text_input("Pronunciation")
    new_kind = st.text_input("Kind of Word")
    new_meaning = st.text_area("Meaning")
    new_collocation = st.text_area("Common Collocation")
    new_synonym = st.text_area("Synonym")
    new_example = st.text_area("Example")
    
    # Submit button
    submitted = st.form_submit_button("Add Flashcard")
    
    # If the form is submitted, add the new flashcard
    if submitted:
        if new_word and new_meaning:  # Ensure word and meaning are provided
            add_new_flashcard(new_word, new_pronounce, new_kind, new_meaning, new_collocation, new_synonym, new_example)
            st.success(f"Flashcard for '{new_word}' added!")
        else:
            st.error("Please provide at least the word and meaning.")

