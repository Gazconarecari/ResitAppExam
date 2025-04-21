import streamlit as st
from supabaseClient import supabase

st.set_page_config(page_title="Resit App")

st.title("Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    response = supabase.table("Users").select("*").eq("email", email).execute()
    users = response.data

    if users and users[0]["password"] == password:
        user = users[0]
        st.session_state["user"] = user
        st.success(f"Logged in as {user['role'].capitalize()}")
        st.switch_page(f"pages/{role_page(user['role'])}")
    else:
        st.error("Invalid email or password")

def role_page(role):
    return {
        "student": "1_StudentDashboard.py",
        "instructor": "2_InstructorDashboard.py",
        "secretary": "3_SecretaryDashboard.py"
    }.get(role, "4_Announcements.py")