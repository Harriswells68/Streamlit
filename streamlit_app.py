
import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(layout="wide")

# Create two columns
col1, col2 = st.columns([1, 1])

with col1:
    # Display the uploaded image
    image = Image.open("https://en.akinator.com/assets/img/akitudes_670x1096/defi.png")
    st.image(image, width=250)

with col2:
    # Display a question with radio buttons
    st.markdown("<h1 style='text-align: center; font-size: 2rem;'>Is your character real?</h1>", unsafe_allow_html=True)
    st.radio(
        "",
        ("Yes", "No", "Don't know", "Probably", "Probably not"),
        horizontal=True,
    )
