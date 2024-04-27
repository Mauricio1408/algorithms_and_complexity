import streamlit as st
from PIL import Image

# Path to local image
image_path = "pages/media/g1.jpg"

img = Image.open(image_path)

st.image(img, caption='', use_column_width=True)

st.header('👋🏽 Welcome!')

st.divider()

st.subheader('A-star Search Algorithm in Graph Traversal')


st.write('Made by:')
st.caption('Mauricio Manuel F. Bergancia\n\nGillie S. Calanuga\n\nMherlie Joy U. Chavez\n\nMichael Rey T. Tuando')

