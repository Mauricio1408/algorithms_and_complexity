import folium.features
import streamlit as st
import folium
import pandas as pd
import plotly.express as px
import sys
import base64

# Path to your local gif file
gif_path = "pages/media/pathfinding_02.gif"

# Open the gif file and encode it
with open(gif_path, "rb") as gif_file:
    contents = gif_file.read()
    data_url = base64.b64encode(contents).decode("utf-8")

# Use the markdown function to display the gif using an HTML img tag
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="gif">', 
    unsafe_allow_html=True
)

from streamlit_folium import st_folium

st.header('') 

# Correct the path if necessary and use single slashes
sys.path.insert(0, 'pages/contents/')
sys.path.insert(0, 'graph_and_heuristics/')

# Import the module (make sure the file name is correct)
import txt_contents, astar_code
import graph_of_iloilo, heuristics

from astar_code import AStarGraph

from graph_of_iloilo import coordinates, get_school

from heuristics import set_heu

st.header('⚒️ Implementation')

st.divider()

st.subheader('Path of the search')

st.write('Below is the geospatial image where the A-star Search Algorithm has explored')

st.caption('Configure settings on the sidebar panel')


#sidebar settings
st.sidebar.header('🌟 A-star Search Algorithm')

st.sidebar.divider()

st.sidebar.subheader('⚙️ Settings')

st.sidebar.write('Tweak the inputs to your liking. The A-star Algorithm smartly finds the way from the start node to the goal node')

st.sidebar.caption('Heuristics and graph are integrated and automatically adjust to the start and goal node you\'ve provided.')

start_node = st.sidebar.selectbox('Start:', ('A - University of the Philippines - Visayas', 'B - University of San Agustin', 'C - Assumption Iloilo', 'D - St. Paul University', 'E - Western Institute of Technology', 'F - West Visayas State University', 'G - Colegio de San Jose', 'H - Saint Vincent Ferrer Seminary', 'I - Central Philippine University'), placeholder='Select Start Node', index=0)

goal_node = st.sidebar.selectbox('Goal:', ('A - University of the Philippines - Visayas', 'B - University of San Agustin', 'C - Assumption Iloilo', 'D - St. Paul University', 'E - Western Institute of Technology', 'F - West Visayas State University', 'G - Colegio de San Jose', 'H - Saint Vincent Ferrer Seminary', 'I - Central Philippine University'),placeholder='Select Goal Node', index=8)

#formatting start_node
def format_start_node(start_node):

    match start_node:

        case 'A - University of the Philippines - Visayas':
            return 'A'
        
        case 'B - University of San Agustin':
            return 'B'
        
        case 'C - Assumption Iloilo':
            return 'C'
        
        case 'D - St. Paul University':
            return 'D'
        
        case 'E - Western Institute of Technology':
            return 'E'
        
        case 'F - West Visayas State University':
            return 'F'
        
        case 'G - Colegio de San Jose':
            return 'G'
        
        case 'H - Saint Vincent Ferrer Seminary':
            return 'H'

        case 'I - Central Philippine University':
            return 'I'

#formatting start_node
def format_goal_node(goal_node):

    match goal_node:

        case 'A - University of the Philippines - Visayas':
            return 'A'
        
        case 'B - University of San Agustin':
            return 'B'
        
        case 'C - Assumption Iloilo':
            return 'C'
        
        case 'D - St. Paul University':
            return 'D'
        
        case 'E - Western Institute of Technology':
            return 'E'
        
        case 'F - West Visayas State University':
            return 'F'
        
        case 'G - Colegio de San Jose':
            return 'G'
        
        case 'H - Saint Vincent Ferrer Seminary':
            return 'H'

        case 'I - Central Philippine University':
            return 'I'

start_node = format_start_node(start_node)
goal_node = format_goal_node(goal_node)
        
heu = set_heu(goal_node)

if goal_node is not None:
    
    st.sidebar.caption(f'Heuristics for goal node: \'{goal_node}\' has been optimized')

show_heu = st.sidebar.toggle('Show Heuristics')

if show_heu:
    st.sidebar.code(heu)

#folium map
astar_path = folium.Map(location=[10.710677132135281, 122.55819550791585], zoom_start=13)

#instantiate graph
iloilo_graph = graph_of_iloilo.set_graph()

show_graph = st.sidebar.toggle('Show Graph')

if show_graph:

    st.sidebar.write(iloilo_graph)

#run A* algo
astar_run  = astar_code.AStarGraph(iloilo_graph, heu)

result = astar_run.a_star_algorithm(start_node, goal_node)

# folium markers
icon_url = 'https://www.flaticon.com/free-icon/location_1483336?term=map+marker&page=1&position=11&origin=tag&related_id=1483336'

icon = folium.features.CustomIcon(icon_url, icon_size=(28, 30))

# Add a marker with the custom icon to every node visited
for index, node in enumerate(result):

    # Define the HTML for the popup with custom styling
    popup_html = f"""
    <div style="font-family: Arial, sans-serif; text-align: center;">
    <span style="font-size: 16px; font-weight: bold;">{index + 1}</span><br>
    {node} - {get_school(node)}
    </div>
    """

    # Create a popup object with the HTML content
    popup = folium.Popup(popup_html, max_width=400)

    folium.Marker(location=coordinates(node), popup=popup).add_to(astar_path)

st_folium(astar_path)

st.write(f'It took the A-star Algorithm {len(result)} steps to finish the search from \'{result[0]}\': {get_school(result[0])} to \'{result[-1]}\': {get_school(result[-1])}')

#map every node explored by A* 
# folium.Marker(location=)
