import streamlit as st
import pandas as pd
from utils.preprocessing import read_file, process_Htask
import warnings

# Suppress FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning)

st.set_page_config(
    page_title="صلة البيت",
    layout="wide",
    initial_sidebar_state="auto",
    page_icon="app/images/selat_albait_favicon.png",
)

# start app by login
# st.switch_page('pages/login.py')


# upload 2 files


# preprocess data and store it in session
h_res = read_file("app/data/h_1-13Sep.csv")
h_res = process_Htask(h_res)
st.session_state["htask_reservations"] = h_res

# booing_res = read_file("app/data/b_1-13Sep.xls", excel=True)
# booing_res = process_Htask(booing_res)
# st.session_state['booking_reservations'] = booing_res


# The dashboard
st.logo("app/images/selat_albait_logo.webp")

st.header('إحصائيات')

pages = [
    st.Page("pages/general.py", title="عامة", icon="📊"),
    st.Page("pages/per_month.py", title=" شهري ", icon="📅"),
    st.Page("pages/reservations.py", title=" الحجوزات ", icon="🕐"),

]


pg = st.navigation(pages)
pg.run()

# apply styling
with open("app/styles.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
