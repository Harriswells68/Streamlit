import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("Akinator")

col1, col2 = st.columns([1, 1])

with col1:
    components.html("""
    <img src="https://en.akinator.com/assets/img/akitudes_670x1096/defi.png" style="width:100%; height:auto;">
    """, height=400)

with col2:
    st.subheader("Is your character real?")
    options = ['Yes', 'No', 'Don\'t know', 'Probably', 'Probably not']
    selected_option = st.radio("Select an option:", options)

    if st.button("Correct"):
        st.success("You got it right!")
