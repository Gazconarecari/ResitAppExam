import streamlit as st
from supabaseClient import supabase

user = st.session_state.get("user")
if not user or user["role"] != "secretary":
    st.error("Unauthorized")
    st.stop()

st.title("Faculty Secretary Dashboard")

with st.form("upload_schedule"):
    course_id = st.number_input("Course ID", step=1)
    date = st.date_input("Exam Date")
    time = st.time_input("Exam Time")
    if st.form_submit_button("Upload Schedule"):
        supabase.table("examschedule").insert({
            "course_id": course_id,
            "date": date.isoformat(),
            "time": time.isoformat(),
            "uploaded_by": user["user_id"]
        }).execute()
        st.success("Schedule uploaded.")