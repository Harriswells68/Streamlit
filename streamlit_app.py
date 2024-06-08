import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
        .css-18e3th9 {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        .css-1d3j6tg {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns([1, 1])

with col1:
    st.image("https://i.imgur.com/4z5tI6g.png", width=250)
    st.markdown(
        """
        <style>
            .css-18e3th9 {
                padding-top: 1rem;
                padding-bottom: 1rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.button("Correct")

with col2:
    st.markdown(
        """
        <style>
            .css-1d3j6tg {
                padding-top: 1rem;
                padding-bottom: 1rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div style="text-align: center;">
        <h1 style="font-size: 2rem;">Is your character real?</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.radio(
        "",
        ("Yes", "No", "Don't know", "Probably", "Probably not"),
        horizontal=True,
    )

st.markdown(
    """
    <style>
        .css-15sduyf {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    .css-18e3th9 {
    padding-top: 1rem;
    padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="text-align: center;">
        <button style="background-color: #f0f0f0; border: none; padding: 1rem 2rem; font-size: 1rem; border-radius: 5px;">Inactive</button>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://en.akinator.com/" style="text-decoration: none;">
            <img src="https://i.imgur.com/pQ0o9Jq.png" alt="Akinator Logo" style="width: 200px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    .css-18e3th9 {
    padding-top: 1rem;
    padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://www.facebook.com/Akinator/" style="text-decoration: none; margin-right: 1rem;">
            <img src="https://i.imgur.com/9g0L439.png" alt="Facebook" style="width: 25px;">
        </a>
        <a href="https://twitter.com/AkinatorGame" style="text-decoration: none; margin-right: 1rem;">
            <img src="https://i.imgur.com/mG2G6yC.png" alt="Twitter" style="width: 25px;">
        </a>
        <a href="https://plus.google.com/+AkinatorGame" style="text-decoration: none;">
            <img src="https://i.imgur.com/6Y7O60N.png" alt="Google Plus" style="width: 25px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
