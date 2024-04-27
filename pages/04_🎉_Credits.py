import streamlit as st
import base64
import requests
from PIL import Image
import io

# Path to your video file
gif_path = r'pages/media/Recording 2024-04-25 164855.gif'

# Open the gif file and encode it
with open(gif_path, "rb") as gif_file:
    contents = gif_file.read()
    data_url = base64.b64encode(contents).decode("utf-8")

# Use the markdown function to display the gif using an HTML img tag
st.markdown(
   f'<img src="data:image/gif;base64,{data_url}" width="600" height="400" alt="gif">', 
    unsafe_allow_html=True
)

# Function to inject custom CSS for centering content in columns
def inject_centered_css():
    st.markdown("""
        <style>
            .column-container { display: flex; justify-content: center; }
            .centered-content { text-align: center; }
        </style>
        """, unsafe_allow_html=True)

# Inject the custom CSS
inject_centered_css()

def show_img(title, img_path, width=None):

    with st.container(height=200, border=True):
        st.caption(title)   
    
        # Path to local image
        image_path = f"{img_path}"

        img = Image.open(image_path)

        if width is None:
            st.image(img, caption='', use_column_width=True)
            pass
        else:
            st.image(img, caption='', width=width)
            pass

st.header('')
st.header('🎉 Credits')

st.divider()

st.subheader('Your help is appreciated and acknowledged')

st.write('The creators of this application would like to thank the following:')

# Create three columns
col1, col2, col3 = st.columns(3)

# Put content in each column
with col1:

    show_img('PavCreations', r'pages/media/Screenshot 2024-04-26 120331.png')

with col2:

    show_img('Github', r"pages/media/github_logo.png")

    show_img('Multiplier', r"pages/media/Screenshot 2024-04-26 122221.png")

with col3:
    
    show_img('West Visayas State University', r"pages/media/WVSU LOGO.PNG", 135)



