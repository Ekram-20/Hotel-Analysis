import streamlit as st
import datetime
from utils import statistics
from components import *

# htask reservations
h_df = st.session_state["htask_reservations"]

# date filter
start_date = h_df["arrival"].min().to_pydatetime()
end_date = h_df["arrival"].max().to_pydatetime()


# st.subheader("الفترة الزمنية")
from_text, to_text, left, right = st.columns(4, vertical_alignment="center")
# from_text.write('من')
right.date_input(" ", value=start_date, min_value=start_date)
# to_text.text('إلى')
left.date_input(" ", value=end_date, max_value=end_date)

# metrics
col1, col2, col3, col4 = st.columns(4)

with col4: metric_card('إجمالي عدد الحجوزات', statistics.number_of_reservations(h_df))
with col3: metric_card('عدد الحجوزات المكتملة', statistics.number_of_active_reservations(h_df))
with col2: metric_card('عدد الحجوزات الملغية', statistics.number_of_cancelled_reservations(h_df))
with col1: metric_card('عدد النزلاء', statistics.number_of_guests(h_df))



# charts
col1, col2 = st.columns(2)
with col1:
    chart_data = statistics.revenue_per_month(h_df)
    box('الايردات شهريا').line_chart(chart_data)

with col2:
    chart_data = statistics.reservations_per_month(h_df)
    box('عدد الحجوزات شهريًا').bar_chart(chart_data, horizontal=True, x_label="عدد الحجوزات")



st.dataframe(h_df)


# apply styling
with open("app/styles.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
