import streamlit as st
from streamlit_lottie import st_lottie
import requests

#load lottie animation
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

lottie_akinaror = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_mj89j8z4.json")

st.set_page_config(page_title="Akinator", page_icon=":genie:")

st.markdown('<style>body{background-color: #c9e7f1;}</style>', unsafe_allow_html=True)
st.title(":genie: Akinator")

col1, col2 = st.columns(2)

with col1:
  st_lottie(lottie_akinaror, speed=1, height=400, key="akinator")

with col2:
  st.write("Is your character real?")
  
  choices = ["Yes", "No", "Don't know", "Probably", "Probably not"]

  choice = st.radio("Select", choices)
  
  if st.button("Correct"):
    st.success("You have guessed correctly!")
