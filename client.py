
import streamlit as st 
import requests 

def e_request(input_text):
    response = requests.post(
    "http://localhost:8000/essay/invoke",
    json={"input":{"topic":input_text}}    
    )

    return response.json()["output"]

def p_request(input_text):
    response = requests.post(
    "http://localhost:8000/poem/invoke",
    json={"input":{"topic":input_text}}    
    )

    return response.json()["output"]


st.title("API Client")
input = st.text_input("Enter the topic")
e_button = st.button("Click for essay")


p_button = st.button("Click for poem")

if input and e_button:
    output = e_request(input)
    st.write(output)

if input and p_button:
    output1 = p_request(input)
    st.write(output1)