import streamlit as st
import pandas as pd
import sys
from PIL import Image

import base64

# Path to your local gif file
gif_path = "pages\media\g3.gif"

# Open the gif file and encode it
with open(gif_path, "rb") as gif_file:
    contents = gif_file.read()
    data_url = base64.b64encode(contents).decode("utf-8")

# Use the markdown function to display the gif using an HTML img tag
st.markdown(
   f'<img src="data:image/gif;base64,{data_url}" width="600" height="400" alt="gif">', 
    unsafe_allow_html=True
)

st.header('')

# Correct the path if necessary and use single slashes
sys.path.insert(0, 'pages/contents/')

# Import the module (make sure the file name is correct)
import txt_contents

# Iloilo Univs DataFrame with latitude and longitude values
data = pd.DataFrame({
    'latitude': [10.698108775421403, 10.702199841325427, 10.70188001238597, 10.702115945215663, 10.711069002902851, 10.713856012683799, 10.721547250653796, 10.721833687480283, 10.731472295086457],
    'longitude': [122.55547754462675, 122.56236990347229, 122.56568846645919, 122.56798284350869, 122.56670318107837, 122.56288379427703, 122.56004524942976, 122.55847496845799, 122.54825537995497],
    'label': ['A - UPV', 'B - USA', 'C - Assumption Iloilo', 'D - St. Paul University', 'E - WIT', 'F - WVSU', 'G - CSJ', 'H - SVF', 'I - CPU']
})

st.header('🌟 About A-Star Search Algorithm')

st.divider()

st.subheader('Unleash the thirst for search within!')

# Call a function from the abt_astar module (replace 'some_function' with the actual function name)
astar_cont = txt_contents.astar_content()

st.caption(astar_cont)

st.divider()

st.subheader('Costs-Costs-Costs. What do they mean?!')

st.code('Actual Cost [g(n)]')

st.caption(txt_contents.a_cost())

st.code('Heuristic Cost [h(n)]')

st.caption(txt_contents.h_cost())

st.code('Total Cost [f(n)]')

st.caption(txt_contents.f_cost())

st.divider()

# Path to your local gif file
gif_path = "D:\Downloads\g4.gif"

# Open the gif file and encode it
with open(gif_path, "rb") as gif_file:
    contents = gif_file.read()
    data_url = base64.b64encode(contents).decode("utf-8")

# Use the markdown function to display the gif using an HTML img tag
st.markdown(
   f'<img src="data:image/gif;base64,{data_url}" width="600" height="400" alt="gif">', 
    unsafe_allow_html=True
)

st.subheader('')

st.subheader('How does it work?')

st.write('To produce the required output, several ways are created to acquire the output of the system. Below are the following guides in running the A* Search Algorithm')

with st.container(height=200, border=True):
    st.subheader('1. Initialize')

    st.divider()

    st.caption(' Initialize a list with the value of nodes from one node to another.')

with st.container(height=200, border=True):
    st.subheader('2. Calculate Heuristic Values')

    st.divider()

    st.caption('Calculate the heuristic values for all nodes in the graph. The heuristic value is an estimation of the cost from a node to the target node.')

with st.container(height=200, border=True):
    st.subheader('3. Select the Starting Node')

    st.divider()

    st.caption('Choose an starting node from the given value. Search Neighboring nodes and go to the one that has the least heuristic value. Mark node as visited.')

with st.container(height=200, border=True):
    st.subheader('4. Repeat Until Target Found')

    st.divider()

    st.caption('Repeat the process until you reach the final node with the shortest distance.')

with st.container(height=200, border=True):
    st.subheader('5. Output')

    st.divider()

    st.caption('This part you can determine the shortest path that can take from the starting node until it reaches the final node.')
