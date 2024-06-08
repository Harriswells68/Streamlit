import streamlit as st

st.set_page_config(layout="wide")

# Create a two-column layout
col1, col2 = st.columns([1, 3])

# Display the image in the first column using HTML
with col1:
    st.markdown(f"""
        <img src="https://en.akinator.com/assets/img/akitudes_670x1096/defi.png" width="250">
    """, unsafe_allow_html=True)

# Display the question asking menu in the second column
with col2:
    st.markdown("# Is your character real?")
    st.markdown("---")
    st.button("Yes")
    st.button("No")
    st.button("Don't know")
    st.button("Probably")
    st.button("Probably not")
