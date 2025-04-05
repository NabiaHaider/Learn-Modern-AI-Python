import streamlit as st  # Streamlit library import karte hain (UI banane ke liye)
import random  # Random module use hota hai random characters generate karne ke liye
import string  # String module se letters, digits aur special characters milte hain

# Function jo password generate karega
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # A-Z aur a-z include kiya gaya hai

    if use_digits:
        characters += string.digits  # Agar user chahe toh 0-9 digits bhi add karo

    if use_special:
        characters += string.punctuation  # Agar user chahe toh special characters bhi add karo

    # Random characters select karke password banaate hain
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI shuru
st.title("Password Generator")  # Page ka title

# Slider for password length (user select kar sakta hai)
length = st.slider("Select password length", min_value=6, max_value=32, value=12)

# Checkboxes for digits aur special characters
use_digits = st.checkbox("Include Digits")  # Agar check kiya toh digits include honge
use_special = st.checkbox("Include Special Characters")  # Agar check kiya toh special characters bhi

# Button jab user click kare to password generate ho
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)  # Password generate karte hain
    st.success(f"Generated Password: `{password}`")  # Successfully generated password show karo

# Ek separator line
st.write("---------------------------------")

# Footer: developer ka naam aur GitHub link
st.markdown("Built with 💖 by [Nabia Haider](https://github.com/NabiaHaider)")
