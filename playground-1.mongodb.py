# Import necessary libraries
from pymongo import MongoClient
from datetime import datetime
import streamlit as st
from langchain.llms import OpenAI
import os
from time import sleep
#Personal library
from APIKEY import apikey


# Set up Streamlit page configuration
st.set_page_config(
    page_title="🦉Fun Fact of the Day",
    page_icon=":owl:", 
    layout="centered",
)

st.markdown(
    """
    <style>
    .stTextInput {
        width: 95%;  # Adjust the width as needed
        font-size: 40px;  # Adjust the font size as needed
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Connect to the MongoDB server
client = MongoClient()

# Select the MongoDB database type
db = client['mongodbVSCodePlaygroundDB']

# Insert fun facts into the MongoDB collection
fun_facts = db['facts']
with open(r"C:\Users\harve\Downloads\Hacks\Funfacts.txt", "r") as file:
    lines = file.readlines()

for line in lines:

    data = {r"C:\Users\harve\Downloads\Hacks\Funfacts.txt": line.strip()}  # Store file paths as data
    fun_facts.insert_one(data)

# Create a dictionary to store fun facts from the file
fun_facts = {}
with open(r"C:\Users\harve\Downloads\Hacks\Funfacts.txt", "r") as file:

    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            date, joke = parts
            fun_facts[date] = joke

# Get the current date and format it
current_date = datetime.now().strftime("%B %d")
current_date = current_date.replace(" 0", " ")
current_fun_fact = fun_facts.get(current_date, "No fun fact found for today.")

# Streamlit app layout
st.title("🦉Daily Fun Fact")
st.subheader("Powered by Streamlit, 🦜️🔗Langchain and MongoDB")
st.subheader(f"The fun fact of today, {current_date}, is:\n {current_fun_fact}")

# Input field for the date
selected_date = st.text_input("Enter a date (e.g., January 1):")

# Display the fun fact if a valid date is entered
if selected_date in fun_facts:
    joke = fun_facts[selected_date]
    st.write(f"Fun Fact for {selected_date}:  {joke}")
else:
    st.write("No joke found for the entered date.")

#Chat GPT fun joke of the day
x=0
while True: 
    st.subheader("🤖ChatGPT Dad Joke of the Day!")
    os.environ['OPENAI_API_KEY'] = apikey
    llm = OpenAI(temperature=1.2)
    response = llm("What is the dad joke for today?")
    st.subheader(response)
    x=x+1
    sleep(45) #31536000
    if (x>=5):
        break