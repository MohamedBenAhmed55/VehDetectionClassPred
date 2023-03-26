import streamlit as st
import plotly
# from st_bridge import bridge, html
from pymongo import MongoClient
import pandas as pd
import numpy as np
from io import StringIO
import datetime

st.header('Data Visualisation for Co2 Emission')
client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
collection = db["mydb"]

data = list(collection.find({}))

co = []
d = []
for doc in data:
    co.append(doc['Average CO2'])
    d.append(doc['date'])

# for doc in data:
#
#     if doc['date'] >= datemin.strftime('%m/%d/%Y') and doc['date'] < datemax.strftime('%m/%d/%Y') :
#         co.append(doc['Average CO2'])
#         d.append(doc['date'])
#     # d.append(doc['date'])


df = pd.DataFrame({
    'date': d,
    'Co2 emission per date': co
})

datemin = st.date_input(
    "from date:",
    datetime.datetime.now().date())

datemax = st.date_input(
    "to date",
    datetime.datetime.now().date())

# dm = '2023-03-03'
# dmx = '2023-03-03'

# def date_filter():
#     return df['date'] > dm

# # date1 = datetime.datetime.now().date()
# date1 = datetime(2023, 3, 3)
# query = {"date": {"$gte": date1}}
# data2 = list(collection.find(query))

# co2 = []
# d2 = []
# for doc in data2:
#     co2.append(doc['Average CO2'])
#     d2.append(doc['date'])

# dff = pd.DataFrame({
#     'date': d,
#     'Co2 emission per date': co
# })
#
# dff = dff.rename(columns={'date': 'index'}).set_index('index')
# dff
# df = list(filter(lambda df: df['date'] >= date1, df))
# filtered_documents = filter(lambda df: df["date"] >= '03-03-2023', df)
# filtered_documents = list(filtered_documents)
# filtered_documents = filtered_documents.rename(columns={'date': 'index'}).set_index('index')
df = df.rename(columns={'date': 'index'}).set_index('index')
st.line_chart(df)
df
# filtered_documents

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)