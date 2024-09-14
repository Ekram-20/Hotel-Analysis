import streamlit as st


# pg = st.navigation([st.Page(''), st.Page("page2.py")])
# pg.run()

pages = {
    # "Your account": [
    #     st.Page("create_account.py", title="Create your account"),
    #     st.Page("manage_account.py", title="Manage your account"),
    # ],
    "مراجع": [
        st.Page("learn.py", title=" تعلم "),
        st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages, position='sidebar')
pg.run()


st.markdown("""
<style>
body, html {
    direction: RTL;
    text-align: right;
}
p, div, input, label, h1, h2, h3, h4, h5, h6 {
    direction: RTL;
    text-align: right;
}

.st-emotion-cache-1tokvoz eczjsme3 {
    display: none;
}

</style>
""", unsafe_allow_html=True)