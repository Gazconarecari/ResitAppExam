import streamlit as st
from supabaseClient import supabase

st.title("Announcements")

announcements = supabase.table("announcements").select("*").execute()
for a in announcements.data:
    st.subheader(a["title"])
    st.write(a["content"])
    st.caption(f"Visible to: {a['visible_to']} | Posted: {a['created_at']}")