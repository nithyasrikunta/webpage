import streamlit as st
import pandas as pd
import sqlite3 as s

# Connect to SQLite database
con = s.connect('Nityadb.db', check_same_thread=False)
cur = con.cursor()
st.write("please enter your details")
# Function to create the web form
def bio():
    st.title("Web Form Example")
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=100, step=1)
    date_of_birth = st.date_input("Date of Birth")
    if st.button("Submit"):
        if email.endswith("gmail.com"):
            df = {
                "NAME": [name],
                "EMAIL": [email],
                "AGE": [age],
                "DOB": [date_of_birth]
            }
            dataframe = pd.DataFrame(df)
            st.write(dataframe)
            return dataframe
        else:
            st.write("Please enter a correct email ending with 'gmail.com'.")
            return None

# Function to insert data into the database
def datadb(input_df):
    if input_df is not None:
        cur.execute("""CREATE TABLE IF NOT EXISTS bio (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(50),
                        email VARCHAR(50),
                        age INTEGER,
                        date_of_birth DATE)""")
        cur.execute("INSERT INTO bio (name, email, age, date_of_birth) VALUES (?, ?, ?, ?)",
                    (input_df.loc[0, "NAME"],  # Access column by name "NAME"
                     input_df.loc[0, "EMAIL"],  # Access column by name "EMAIL"
                     int(input_df.loc[0, "AGE"]),  # Access column by name "AGE"
                     input_df.loc[0, "DOB"]))  # Access column by name "DOB"
        con.commit()

# Get input DataFrame from bio function and insert into database
input_df = bio()
datadb(input_df)

# Close database connection
con.close()
