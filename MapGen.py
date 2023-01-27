import folium
import pandas as pd
from folium.plugins import HeatMap


# Load data from file
data = pd.read_csv('2023-01-22 Walking.rctrk', skiprows=1, delimiter='\t')

# Create map object
m = folium.Map(location=[data.Latitude.mean(), data.Longitude.mean()], zoom_start=15)

# Create heatmap overlay
HeatMap(data[['Latitude', 'Longitude', 'DoseRate']], overlay=True, name='Dose Rate', 
        control=True, show=True, blur=20, opacity=0.01).add_to(m)

# Add layer control to toggle heatmap overlay
folium.LayerControl().add_to(m)

m.save('map.html')
