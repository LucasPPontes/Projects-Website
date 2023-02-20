import streamlit as st 
import components as cp

st.markdown("# Esse pequeno projeto realiza um scan em um site e retorna algumas informações importantes sobre ele")
st.markdown("#### Digite o endreço do site para conseguir coletar as informações Ex: www.google.com")
site = st.text_input("Site: ")
confirm_button = st.button("Ok")

if confirm_button:
    st.write(cp.ip_target(site))
    st.write(cp.who_is(site))