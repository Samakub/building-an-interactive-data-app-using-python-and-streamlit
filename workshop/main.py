import pandas as pd
import streamlit as st
import plotly.express as px

st.title("My First Streamlit App")
st.header("Hello World 👏")
st.write("This is an example of a simple Streamlit app.")

df = pd.read_csv("../datasets/1642645053.csv", encoding="tis-620")
st.write(df)

data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/titanic.csv"  # ตัวอย่างลิงก์ CSV
df = pd.read_csv(data_url)
st.write(df)

image_url = "https://du.lnwfile.com/169w1m.png"
st.write("### Example Image from URL")
st.image(image_url, caption="This is an example image from URL", use_column_width=True)

rating = st.radio(
    "How would you rate this class?",
    ("1", "2", "3", "4", "5")
)
st.write(f"You selected {rating}")
number = st.slider("Select a number", 0, 100, 50)
st.write("The current number is ", number)

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

df = pd.read_csv(url)
df_grouped_by_species = df.groupby("species")["body_mass_g"].mean()
st.bar_chart(df_grouped_by_species)


fig = px.bar(df_grouped_by_species.reset_index(), x="species", y="body_mass_g")
st.plotly_chart(fig)

with st.sidebar:
    st.write("This is a sidebar")
    option = st.selectbox(
        "Which number do you like best?",
        ["1", "2", "3", "4", "5"]
    )