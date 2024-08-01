import streamlit as st
from streamlit_supabase_auth import login_form, logout_button

session = login_form(
    url="https://jhpdalsdsiwhgtnlfevz.supabase.co",
    apiKey= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpocGRhbHNkc2l3aGd0bmxmZXZ6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjA2MzM2ODgsImV4cCI6MjAzNjIwOTY4OH0.FaTT1L6_nqtyXn8wUMFKgfi4SACUuLaD08CC9kE6Utk",
    providers=["apple", "facebook", "github", "google"],
)
print(F"{session}")

if session:
    supabase_session= st.session_state.supabase_client.auth.get_session()
    st.write({supabase_session})
if not session:
    st.write("not session") 

# Update query param to reset url fragments
st.query_params.page="success"
with st.sidebar:
    st.write(f"Wellcome {st.query_params.page}")
    #st.write(f"Welcome {session['user']['email']}")
    logout_button()