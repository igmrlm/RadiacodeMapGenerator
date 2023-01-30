# RadiacodeMapGenerator
This code uses the folium library to create a heatmap overlay of walking dose rate data on an interactive map. The data is loaded from a .rctrk file and plotted on a map centered at the mean coordinates of the data points. The heatmap is customizable with options for blur, opacity, and visibility.

# Usage

python heatmap_generator.py [input file name] [options]
# Options

--zoom       Map zoom level (default: 15)
--blur       Heatmap blur level (default: 20)
--opacity    Heatmap opacity (default: 0.01)
# Example

python heatmap_generator.py data.txt --zoom 12 --blur 15 --opacity 0.05

# Requirements
folium
pandas
argparse
webbrowser

# Output
The script generates an HTML file named "map.html" which displays the heatmap and opens it in the system's default web browser.
