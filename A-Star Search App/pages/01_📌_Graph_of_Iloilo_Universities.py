import streamlit as st
import folium
import pandas as pd
import plotly.express as px
import sys
from PIL import Image

# Path to local image
image_path = "D:\Downloads\g2.jpg"

img = Image.open(image_path)

st.image(img, caption='', use_column_width=True)

from streamlit_folium import st_folium

# Correct the path if necessary and use single slashes
sys.path.insert(0, 'pages/contents/')

# Import the module (make sure the file name is correct)
import txt_contents

# Iloilo Univs DataFrame with latitude and longitude values
data = pd.DataFrame({
    'latitude': [10.698108775421403, 10.702199841325427, 10.70188001238597, 10.702115945215663, 10.711069002902851, 10.713856012683799, 10.721547250653796, 10.721833687480283, 10.731472295086457],
    'longitude': [122.55547754462675, 122.56236990347229, 122.56568846645919, 122.56798284350869, 122.56670318107837, 122.56288379427703, 122.56004524942976, 122.55847496845799, 122.54825537995497],
    'label' : ['A - UPV', 'B - USA','C - Assumption Iloilo', 'D - St. Paul University','E - WIT', 'F - WVSU','G - CSJ', 'H - SVF', 'I - CPU']
})

st.header('📌 Graph of Iloilo Universities')

st.divider()

st.subheader('Iloilo here we come!')

st.write('We have plotted 9 universities and colleges in Iloilo City from General Luna street to Jaro, Iloilo.')

with st.expander("See the list of universities"):
    st.write('University of the Philippines - Visayas')
    st.write('University of San Agustin')
    st.write('Assumption Iloilo')
    st.write('St. Paul University')
    st.write('Western Institute of Technology')
    st.write('West Visayas State University')
    st.write('Colegio de San Jose')
    st.write('Saint Vincent Ferrer Seminary')
    st.write('Central Philippine University')


# fig = px.scatter_mapbox(data, lat="latitude", lon="longitude",
#                         hover_name="label", zoom=3, height=300)

# fig.update_layout(mapbox_style="open-street-map")
# fig.update_traces(marker=dict(size=10))
# st.plotly_chart(fig)

# Display the map with the data points
st.map(data)

cont = txt_contents.abt_map()

st.caption(cont)

