import streamlit as st
from supabaseClient import supabase

user = st.session_state.get("user")
if not user or user["role"] != "student":
    st.error("Unauthorized")
    st.stop()

st.title("Student Dashboard")

data = supabase.table("enrollments").select("*").eq("student_id", user["user_id"]).execute()
for record in data.data:
    st.write(f"Course ID: {record['course_id']} | Grade: {record['grade']}")
    if record["eligible_for_resit"] and not record["declared_resit"]:
        if st.button(f"I want to take resit for course {record['course_id']}", key=record["enrollment_id"]):
            supabase.table("enrollments").update({"declared_resit": True}).eq("enrollment_id", record["enrollment_id"]).execute()
            st.success("You are registered for the resit.")