import streamlit as st
from PIL import Image

st.set_page_config(page_title="Admin Dashboard", page_icon=":guardsman:")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5F5F5;
    }
    .stButton>button {
        background-color: #3498db;
        color: #ffffff;
        border-radius: 20px;
        border: none;
        font-size: 16px;
        font-weight: bold;
        padding: 10px 20px;
        margin-right: 10px;
    }
    .stCheckbox>div>label {
        font-size: 16px;
        font-weight: bold;
        color: #000000;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# image = Image.open("header.png")
# st.image(image, use_column_width=True)

st.write(
    """
    # Admin Dashboard
    Use the toggles below to manage the prediction model and the driver dashboard.
    """
)

enable_prediction = st.checkbox("Enable/Disable prediction model")

train_model = st.checkbox("Train prediction model")

deactivate_dashboard = st.checkbox("Deactivate Driver Dashboard")

st.write("---")

st.write("## Status")
st.write("Enable/Disable prediction model:", enable_prediction)
st.write("Train prediction model:", train_model)
st.write("Deactivate Driver Dashboard:", deactivate_dashboard)

# image = Image.open("footer.png")
# st.image(image, use_column_width=True)