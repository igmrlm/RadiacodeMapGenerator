# RadiacodeMapGenerator
This code uses the folium library to create a heatmap overlay of walking dose rate data on an interactive map. The data is loaded from a .rctrk file and plotted on a map centered at the mean coordinates of the data points. The heatmap is customizable with options for blur, opacity, and visibility.

There are issues with this code.. It's making a heatmap based on the density of the points instead of the measured dose rate of those points and I'm not sure how to fix it yet.

# Usage

python MapGen.py [input file name] [options]
# Options

-z, --zoom       Map zoom level (default: 15)

-b, --blur       Heatmap blur level (default: 20)

-o, --opacity    Heatmap opacity (default: 0.01)

# Example

python MapGen.py track.rctrk -z 12 -b 15 -o 0.05

# Requirements
folium
pandas
argparse
webbrowser

# Output
The script generates an HTML file named "map.html" which displays the heatmap and opens it in the system's default web browser.
