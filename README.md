# DensityHeatMapGen.py 

This code uses the folium library to create a heatmap overlay of walking dose rate data on an interactive map. The data is loaded from a .rctrk file and plotted on a map centered at the mean coordinates of the data points. The heatmap is customizable with options for blur, opacity, and visibility.

There are issues with this code.. It's making a heatmap based on the density of the points instead of the measured dose rate of those points 

This file was my first attempt to create an interpolated map. It was a good learning experience but it is not generated a map based on doserate -- instead it's generating  based on measurement density, which in my opinion is basically useless for this specific use case of creating maps for a radiacode101.
Currently it's generating the heatmap based on a concentration of points instead of doserate values, see more here if you want to learn about that:

https://gis.stackexchange.com/questions/256/building-effective-heat-maps
# Usage

python DensityHeatMapGen.py [input file name] [options]
# Options

-z, --zoom       Map zoom level (default: 15)

-b, --blur       Heatmap blur level (default: 20)

-o, --opacity    Heatmap opacity (default: 0.01)

# Example

python DensityHeatMapGen.py track.rctrk -z 12 -b 15 -o 0.05

# Requirements
folium
pandas
argparse
webbrowser

# Output
The script generates an HTML file named "map.html" which displays the heatmap and opens it in the system's default web browser.
