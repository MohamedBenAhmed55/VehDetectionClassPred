import streamlit as st
# from st_bridge import bridge, html
from pymongo import MongoClient
import pandas as pd
import numpy as np
from io import StringIO
import datetime
import plotly.express as px

st.set_page_config(page_title="Driver Dashboard", page_icon=":guardsman:")
st.header('Data Visualisation for Co2 Emission')
client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
collection = db["mydb"]

data = list(collection.find({}))

co = []
d = []
d2 = []
co2 = []
for doc in data:
    co.append(doc['Average CO2'])
    d.append(doc['date'])

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

date_format = "%Y-%m-%d"

# date1 = "2023-02-24"
# date2 = "2023-03-24"
date1 = datemin.strftime('%Y-%m-%d')
date2 = datemax.strftime('%Y-%m-%d')
datemin = datetime.datetime.strptime(date1, date_format)
datemax = datetime.datetime.strptime(date2, date_format)

for doc in data:
    date_string = doc['date']
    date_obj = datetime.datetime.strptime(date_string, date_format)

    if date_obj >= datemin and date_obj <= datemax  :
        co2.append(doc['Average CO2'])
        d2.append(doc['date'])

# d2
df2 = pd.DataFrame({
    'date': d2,
    'Co2 emission per date': co2
})

df2 = df2.rename(columns={'date': 'index'}).set_index('index')
st.line_chart(df2)
df2

# df = df.rename(columns={'date': 'index'}).set_index('index')
# st.line_chart(df)
# df

st.header('Data Visualisation for Co2 Emission per vehicle type')
collection = db["mydb2"]
data = list(collection.find({}))
df = pd.DataFrame(data)

car = []

for doc in data:
    date_string = doc['date']
    date_obj = datetime.datetime.strptime(date_string, date_format)

    if date_obj >= datemin and date_obj <= datemax:
        car.append(doc)

df2 = pd.DataFrame(car)

plot_data = df2[["hatchback Co2", "pickup Co2", "sedan Co2", "suv Co2", "Average CO2", "date"]]
fig = px.line(plot_data, x="date", y=["hatchback Co2", "pickup Co2", "sedan Co2", "suv Co2", "Average CO2"],
              labels={"value": "CO2 Emissions (g/km)", "date": "Date"},
              title="CO2 Emissions by Car Type",
              width=800, height=500)
st.plotly_chart(fig)
plot_data

st.header('Data Visualisation for Co2 Emission Predicted in the next week')
collection = db["mydb3"]

data = list(collection.find({}))

pred= []
co22 =[]
d3 = []
for doc in data:
    date_string = doc['date']
    date_obj = datetime.datetime.strptime(date_string, date_format)

    if date_obj >= datemin and date_obj <= datemax:
        co22.append(doc['Prediction'])
        d3.append(doc['date'])

df2 = pd.DataFrame({
    'date': d3,
    'Prediction': co22
})

plot_data = df2[["Prediction", "date"]]
fig = px.line(plot_data, x="date", y=["Prediction"],
              labels={"value": "CO2 Emissions (g/km)", "date": "Date"},
              title="CO2 Emissions in the next week",
              width=800, height=500)
st.plotly_chart(fig)
df2

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     # To read file as bytes:
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)
#
#     # To convert to a string based IO:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     st.write(stringio)
#
#     # To read file as string:
#     string_data = stringio.read()
#     st.write(string_data)
#
#     # Can be used wherever a "file-like" object is accepted:
#     dataframe = pd.read_csv(uploaded_file)
#     st.write(dataframe)
