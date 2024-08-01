import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query

# Initialize connection.
st_supabase = st.connection(
    name="supabase_connection", 
    type=SupabaseConnection, 
    ttl=None,
    url="https://jhpdalsdsiwhgtnlfevz.supabase.co",
    key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpocGRhbHNkc2l3aGd0bmxmZXZ6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjA2MzM2ODgsImV4cCI6MjAzNjIwOTY4OH0.FaTT1L6_nqtyXn8wUMFKgfi4SACUuLaD08CC9kE6Utk",
)

# Perform query.
rows=execute_query(st_supabase.table("Users").select("*").order("username",desc=True), ttl="1m")
print(F"rows={rows}")

# Print results.
st.markdown("## Users")

for row in rows.data:
    st.write(f"{row['username']} ; {row['identity']} ; {row['password']} ; {row['roleId']} ; {row['city']}")


st.dataframe(rows.data)
#st.data_editor(rows.data)
