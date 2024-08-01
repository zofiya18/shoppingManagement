import streamlit as st
#from streamlit_login  import login_form
from st_login_form import login_form
import subprocess
import shopping_list_screen

client = login_form(user_tablename="Users")

if st.session_state["authenticated"]:
    if st.session_state["username"]:
        st.success(f"Welcome {st.session_state['username']}")
        subprocess.call(['python', 'shopping_list_screen.py'])
    else:
        st.success("Welcome guest")
else:
    st.error("Not authenticated")