import folium
import pandas as pd
import argparse
from folium.plugins import HeatMap
import webbrowser

# Define argparse for options
parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='Input file name')
parser.add_argument('-z', '--zoom', type=int, help='Map zoom level', default=15)
parser.add_argument('-b', '--blur', type=int, help='Heatmap blur level', default=20)
parser.add_argument('-o', '--opacity', type=float, help='Heatmap opacity', default=0.01)

args = parser.parse_args()

# Print out settings for run

print(f"Now generating map from:\t{args.file}\nHeatMap blur level:\t\t{args.blur}\nHeatmap opacity:\t\t{args.opacity}\nMap zoom level:\t\t\t{args.zoom}")


# Load data from file
data = pd.read_csv(args.file, skiprows=1, delimiter='\t')

# Create map object
m = folium.Map(location=[data.Latitude.mean(), data.Longitude.mean()], zoom_start=args.zoom)

# Create heatmap overlay
HeatMap(data[['Latitude', 'Longitude', 'DoseRate']], overlay=True, name='Dose Rate',
control=True, show=True, blur=args.blur, opacity=args.opacity).add_to(m)

# Add layer control to toggle heatmap overlay
folium.LayerControl().add_to(m)

m.save('map.html')

# Open in the System default webbrowser
webbrowser.open('map.html')
