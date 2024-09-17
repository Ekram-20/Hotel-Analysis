import streamlit as st


def box(title, height=400):
    container = st.container(border=True, height=height)
    container.write(title)
    return container


def metric_card(label, value):
    container = st.container(border=True, height=100)
    container.write(label)
    container.write(value)
    return container
