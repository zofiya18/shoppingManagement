import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection.
st_supabase = st.connection(
    name="supabase_connection", 
    type=SupabaseConnection, 
    ttl=None,
    url="https://jhpdalsdsiwhgtnlfevz.supabase.co",
    key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpocGRhbHNkc2l3aGd0bmxmZXZ6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjA2MzM2ODgsImV4cCI6MjAzNjIwOTY4OH0.FaTT1L6_nqtyXn8wUMFKgfi4SACUuLaD08CC9kE6Utk",
)

#conn = st.connection("supabase",type=SupabaseConnection)
#print({conn._secrets.get()})
# Perform query.
#rows1=execute_query(st_supabase.table("Users").select("*", count="None").order("name",desc=True), ttl="1m")
rows = st_supabase.query("*", table="Users", ttl="1m").execute()
print(F"rows={rows}")

# Print results.
for row in rows.data:
    st.write(f"{row['name']} : {row['password']}")