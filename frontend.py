import streamlit as st
from agent import qa_chain

st.title("MEDI-BOT")
st.write("Ask any queries about diseases")

user_input = st.text_area("Enter the disease", height=100)

if st.button("SEARCH"):
    if user_input.strip():
        response=qa_chain.invoke(user_input)
        st.write("ANSWER")
        st.markdown(response['result'])
    else:
        st.write("No Query Passed")
            
