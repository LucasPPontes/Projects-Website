import streamlit as st 
from PIL import Image

st.markdown("# Esse pequeno projeto visa automatizar a criação de containers no docker")
st.markdown("## Futuramente a idéia é melhorar essa automação com mais recursos")
st.button("Visualizar projeto no Github",)

home = Image.open("images/dockerpy/home.png")
first_img = Image.open("images/dockerpy/1.png")
second_img = Image.open("images/dockerpy/2.png")
third_img = Image.open("images/dockerpy/3.png")
fourth_img = Image.open("images/dockerpy/4.png")

st.image(home)

st.markdown("## Existem 4 opções disponíveis para escolha")

st.markdown("#### Opção 1 roda um container")
st.image(first_img)

st.markdown("#### Opção 2 verifica quais são os containers ativos")
st.image(second_img)

st.markdown("#### Opção 3 mostra todas as imagens docker existentes")
st.image(third_img)

st.markdown("#### Opção 4 mostra todos os containers que foram executados")
st.image(fourth_img)



