import streamlit as st
from supabaseClient import supabase

user = st.session_state.get("user")
if not user or user["role"] != "instructor":
    st.error("Unauthorized")
    st.stop()

st.title("Instructor Dashboard")

courses = supabase.table("courses").select("*").eq("instructor_id", user["user_id"]).execute()

for course in courses.data:
    st.subheader(course["course_name"])
    st.markdown("### Exam Details")
    existing = supabase.table("examdetails").select("*").eq("course_id", course["course_id"]).execute()
    if existing.data:
        st.json(existing.data[0])
    else:
        with st.form(f"details_{course['course_id']}"):
            exam_type = st.text_input("Exam type")
            num_questions = st.number_input("Number of questions", step=1)
            calculator_allowed = st.checkbox("Calculator allowed?")
            notes = st.text_area("Notes")
            if st.form_submit_button("Save"):
                supabase.table("examdetails").insert({
                    "course_id": course["course_id"],
                    "exam_type": exam_type,
                    "num_questions": num_questions,
                    "calculator_allowed": calculator_allowed,
                    "notes": notes
                }).execute()
                st.success("Exam details saved.")