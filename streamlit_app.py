import streamlit as st

component = """
<div style="display: flex; flex-direction: row;">
    <div style="width: 40%; padding: 10px;">
        <img src="https://en.akinator.com/assets/img/akitudes_670x1096/defi.png" style="width:100%; height:auto;">
    </div>
    <div style="width: 60%; padding: 10px;">
        <h2>Akinator</h2>
        <p>Is your character real?</p>
        <form>
            <input type="radio" id="yes" name="option" value="Yes">
            <label for="yes">Yes</label><br>
            <input type="radio" id="no" name="option" value="No">
            <label for="no">No</label><br>
            <input type="radio" id="dont_know" name="option" value="Don't know">
            <label for="dont_know">Don't know</label><br>
            <input type="radio" id="probably" name="option" value="Probably">
            <label for="probably">Probably</label><br>
            <input type="radio" id="probably_not" name="option" value="Probably not">
            <label for="probably_not">Probably not</label><br>
        </form>
        <button style="background-color: #4CAF50; color: #ffffff; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Correct</button>
    </div>
</div>
"""

st.components.v1.html(component, height=670)
