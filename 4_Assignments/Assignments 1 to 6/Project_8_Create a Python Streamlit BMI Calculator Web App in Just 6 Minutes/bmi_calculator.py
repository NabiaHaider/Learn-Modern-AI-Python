import streamlit as st

# Title of the app
st.title("BMI Calculator")

# User Input: Weight (in kilograms) and Height (in meters)
weight = st.number_input("Enter your weight (in kg):", min_value=1.0)
height = st.number_input("Enter your height (in meters):", min_value=0.1)

# Calculate BMI when both weight and height are provided
if weight and height:
    bmi = weight / (height ** 2)
    
    # Display BMI result
    st.write(f"Your BMI is: {bmi:.2f}")
    
    # BMI category
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")





# 1. Importing Streamlit:

#  import streamlit as st
# a.Streamlit ek Python library hai jo aapko interactive web apps banaane ki suvidha deti hai.
# b.Hum yahan streamlit ko import kar rahe hain aur st ka alias (short name) use kar rahe hain.

# 2. App ka Title:

# st.title("BMI Calculator")
# a.st.title() ek function hai jo web page pe app ka title set karta hai. Yahan, humne app ka title "BMI Calculator" rakha hai.
# b.Jab aap app ko run karenge, yeh title web page pe top par dikhayi dega.

# 3. User Input (Weight aur Height):

# weight = st.number_input("Enter your weight (in kg):", min_value=1.0)
# height = st.number_input("Enter your height (in meters):", min_value=0.1)

# a.st.number_input() Streamlit ka function hai jo user se number input lene ke liye use hota hai.
# b.weight aur height ko user se input lene ke liye use kiya gaya hai:
# c.min_value=1.0 ka matlab hai ke weight minimum 1 kg ho sakta hai.
# d.min_value=0.1 ka matlab hai ke height minimum 0.1 meter ho sakti hai.

# 4. BMI Calculate Karna:

# if weight and height:
#     bmi = weight / (height ** 2)
# a.Yeh if condition check karti hai ke agar weight aur height dono diye gaye hain, tab hi BMI calculate kiya jayega.

# BMI ka formula:

# BMI
# =
# weight
# height
# 2
# BMI= 
# height 
# 2
 
# weight
# ​
 
# Matlab, weight ko height ke square se divide kiya jata hai.

# 5. BMI Result Display Karna:

# st.write(f"Your BMI is: {bmi:.2f}")
# a.st.write() function ka use hum kisi bhi result ko screen pe display karne ke liye karte hain.
# b.Yahan f"Your BMI is: {bmi:.2f}" ke saath, hum BMI ko format kar rahe hain jisme 2 decimal places tak value dikhayi jayegi.

# 6. BMI Category (Underweight, Normal, Overweight, Obese):

# if bmi < 18.5:
#     st.write("You are underweight.")
# elif 18.5 <= bmi < 24.9:
#     st.write("You have a normal weight.")
# elif 25 <= bmi < 29.9:
#     st.write("You are overweight.")
# else:
#     st.write("You are obese.")
# BMI ke value ke hisaab se, yeh code user ko category bata raha hai:

# Underweight: Agar BMI 18.5 se kam hai.

# Normal Weight: Agar BMI 18.5 se 24.9 ke beech hai.

# Overweight: Agar BMI 25 se 29.9 ke beech hai.

# Obese: Agar BMI 30 ya usse zyada hai.

# elif ka matlab hai agar pehla condition false ho, toh doosra check kiya jayega.

# Example:
# Agar aapka weight 70 kg aur height 1.75 meters hai:

# BMI calculate hoga:

# 𝐵
# 𝑀
# 𝐼
# =
# 70
# (
# 1.75
# )
# 2
# =
# 22.86
# BMI= 
# (1.75) 
# 2
 
# 70
# ​
#  =22.86
# Web app user ko dikhayega:
# "Your BMI is: 22.86"
# "You have a normal weight."

