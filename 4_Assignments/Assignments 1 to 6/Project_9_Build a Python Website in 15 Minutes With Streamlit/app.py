import streamlit as st

# Title of the website
st.title("Welcome to My Simple Python Website")

# Display a brief description
st.write("""
This is a simple Python website created using Streamlit. 
It allows you to enter your name and age, and it will tell you your birth year.
""")

# Input fields
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=150)

# Calculate and display the birth year
if name and age:
    birth_year = 2025 - age  # Assuming the current year is 2025
    st.write(f"Hello {name}, you were born in {birth_year}.")



# st.title(): Website ka title display karega.

# st.write(): Description ko website pe display karega.

# st.text_input(): User se naam input lene ke liye.

# st.number_input(): User se age input lene ke liye.

# Birth Year Calculation: Hum 2025 ko current year maan kar birth year calculate kar rahe hain (aap current year ko dynamically 
# fetch kar sakte hain agar chahein).