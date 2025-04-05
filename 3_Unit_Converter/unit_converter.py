import streamlit as st  # Streamlit library import kar rahe hain (UI banane ke liye)

# Function jo units ko convert karega
def convert_units(value, unit_from, unit_to):
    # Sab possible conversions aur unki values yahan define ki gayi hain
    conversions = {
        "meter_kilometer": 0.001,  # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000,   # 1 kilometer = 1000 meters
        "gram_kilogram": 0.001,    # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000,     # 1 kilogram = 1000 grams 
    }

    key = f"{unit_from}_{unit_to}"  # Input aur output units se ek key banate hain (jaise "meter_kilometer")

    if key in conversions:  # Agar conversion key available hai
        return value * conversions[key]  # Value ko multiply karte hain conversion factor se
    else:
        return "Conversion not available"  # Agar conversion available nahi hai toh message return karo

# Streamlit ka UI title
st.title("Unit Converter")  # Page ka title

# User se numeric value input lena (0 se choti value allowed nahi)
value = st.number_input("Enter the Value", min_value=0.0, format="%.2f")  # Do decimal places tak input allow hai

# User ko unit select karne ka option (from)
unit_from = st.selectbox("Convert From:", ["meter", "kilometer", "gram", "kilogram"])

# User ko unit select karne ka option (to)
unit_to = st.selectbox("Convert To:", ["meter", "kilometer", "gram", "kilogram"])

# Jab user 'Convert' button par click kare
if st.button('Convert'):
    result = convert_units(value, unit_from, unit_to)  # Conversion function ko call karo
    st.write(f"Converted Value: {result}")  # Result display karo
