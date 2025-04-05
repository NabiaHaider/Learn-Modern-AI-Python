import streamlit as st  # Streamlit library import karte hain, jo UI banane ke liye use hoti hai
import pandas as pd  # Pandas library import karte hain data processing ke liye
import os  # OS module file path handle karne ke liye
from io import BytesIO  # BytesIO memory buffer banata hai for file downloads

# App ka page set karte hain
st.set_page_config(page_title="💿Data Sweeper", layout="wide")
st.title(" 💿Data Sweeper")  # App ka title dikhate hain
st.write("Transfrom your files between CSV and Excel formats with built-in data cleaning and visiualization!.")  # Description

# File upload karne ka UI
uploaded_files = st.file_uploader("Upload a CSV file (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

# Agar files upload ki gayi hain
if uploaded_files:
    for file in uploaded_files:  # Har file ko loop mein process karte hain
        file_ext = os.path.splitext(file.name)[-1].lower()  # File extension nikalte hain

        if file_ext == ".csv":
            df = pd.read_csv(file)  # CSV file ko read karte hain
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)  # Excel file ko read karte hain
        else:
            st.error(f"❌File type not stopped. Please upload a CSV or Excel File.{file_ext}")  # Invalid file type error
            continue  # Next file process karo

        # File ka naam aur size show karte hain
        st.write(f" **File Name:** {file.name}")
        st.write(f" **File Size:** {file.size / 1024}")  # Size in KB

        if df is not None:  # Agar dataframe load hua ho
            # Top 5 rows show karte hain
            st.write("🔍Preview the Head of the Dataframe")
            st.dataframe(df.head())

            # Data cleaning section
            st.subheader("🧹Data Cleaning Options")
            if st.checkbox(f"Clean Data for {file.name}"):  # Checkbox for enabling cleaning
                col1, col2 = st.columns(2)  # 2 columns mein options show karte hain

                with col1:
                    if st.button(f"Remove Duplicates from {file.name}"):  # Duplicate hatane ka button
                        df.drop_duplicates(inplace=True)  # Duplicates hata do
                        st.write("✅ Duplicates Removed!")

                with col2:
                    if st.button(f"Fill Missing Values for {file.name}"):  # Missing values fill karne ka button
                        numeric_cols = df.select_dtypes(include=['number']).columns  # Numeric columns chunte hain
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())  # Mean se fill karte hain
                        st.write("✅ Missing Values Filled!")

                # Column selection for conversion
                st.subheader("🎯Select Columns to Convert")
                columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
                df = df[columns]  # Sirf selected columns ko rakhte hain

                # Data visualization
                st.subheader("📊 Data Visualization")
                if st.checkbox(f"Show Visualizations for {file.name}"):  # Visualization checkbox
                    st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])  # Bar chart for first 2 numeric columns

                # File conversion options
                st.subheader(" 🔄Conversion Options")
                conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)  # Radio button for file type

                if st.button(f"Convert {file.name}"):  # Conversion button
                    buffer = BytesIO()  # Temporary memory buffer create karte hain
                    if conversion_type == "CSV":
                        df.to_csv(buffer, index=False)  # Data ko CSV format mein convert karte hain
                        buffer.seek(0)  # Buffer ko reset karte hain
                        new_file_name = file.name.replace(file_ext, ".csv")  # Naya naam banate hain
                        mime_type = "text/csv"

                    elif conversion_type == "Excel":
                        df.to_excel(buffer, index=False)  # Excel format mein convert karte hain
                        buffer.seek(0)  # Buffer ko reset karte hain
                        new_file_name = file.name.replace(file_ext, ".xlsx")
                        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                    # Download button
                    st.download_button(
                        label=f"⬇ Download {new_file_name}",  # Button label
                        data=buffer,  # Data buffer
                        file_name=new_file_name,  # File ka naam
                        mime=mime_type  # MIME type for file
                    )

                    st.success("✅All files processed Successfully!")  # Success message
