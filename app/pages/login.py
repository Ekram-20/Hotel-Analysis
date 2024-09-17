
import streamlit as st

st.image('app/images/selat_albait_logo.jpeg')

with st.form("my_form"):
    st.header('login')

    username = st.text_input("Form slider")
    password = st.text_input("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", username, "checkbox", password)
