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
rows=execute_query(st_supabase.table("Shopping").select("*").order("dateCreated",desc=True), ttl="1m")
print(F"rows={rows}")

st.markdown("## רשימת קניות")

# Print results.
c1, c2, c3, c4, c5, c6 = st.columns([1,2,2,1,3,3])
with st.container():
    c1.markdown("###### מס''ד")
    c2.markdown("###### שם מוצר")
    c3.markdown("###### חברה")
    c4.markdown("###### כמות")
    c5.markdown("###### הערה")
    c6.markdown("###### תאריך יצירה")
for row in rows.data:
    c1.write(f"{row['id']}")
    c2.write(f"{row['productName']}")
    c3.write(f"{row['companyName']}")
    c4.write(f"{row['count']}")
    c5.write(f"{row['remark']}")
    c6.write(f"{row['dateCreated']}")
             
#st.dataframe(rows.data)

def saveNewProduct():
    newProduct=execute_query(st_supabase.table("Shopping")
                     .insert([{"productName": "אקנומיקה", "companyName": "סנו גאוול"
                              , "count": "2", "remark":"אקנומיקה סמיכה"}]), ttl="1m")
    st.text("##### !המוצר נוסף בהצלחה")


def addProductClicked():
    p1,p2,p3,p4=st.columns([2,2,1,3])
    p1.text_input('שם מוצר', key='productName')
    p2.text_input('שם חברה', key='companyName')
    p3.text_input('כמות', key='count')
    p4.text_input('הערה', key='remark')
    st.button('הוסף', key='insertPrduct',on_click=saveNewProduct)


st.button('הוסף מוצר חדש', key='addProduct',on_click=addProductClicked)
