# NewMapGen.py

python generate_heatmap.py <data_input_file> [--no-points] [--scale-factor <value>] [--no-normalization]


# MapGen.py

MapGen is a simple Python script that plots data from a radiacode101 track file with the ability to adjust several display and output options.

## Requirements
* Python 3
* pandas
* numpy
* matplotlib

## Usage

python MapGen.py [file] [-a] [-m] [-g [grid_size]] [-c [cmap]] [-d [dpi]] [-v] [-s] [-f [font_size]]


## Options
* `file`: Input file name (required)
* `-a`/`--annotations`: Enables plot annotations
* `-m`/`--marker`: Disables the circular marker
* `-g`/`--grid_size`: Grid size (default: 500)
* `-c`/`--cmap`: Colormap type (default: 'jet')
* `-d`/`--dpi`: dpi of the saved image (default: 500)
* `-v`/`--view`: Enables plot.show()
* `-s`/`--save`: Enables plot.savefig()
* `-f`/`--font_size`: Annotation font size (default: 8)

## Examples

python MapGen.py track.rctrk -a -m -v

This will plot the data in track.rctrk, with annotations enabled and markers disabled, and display it on the screen.

python MapGen.py track.rctrk -s

This will plot the data in track.rctrk and save it as `map.png` in the working directory.

python MapGen.py track.rctrk -g 1000 -c viridis -f 10 -d 300 -v

This will plot the data in track.rctrk, with grid size 1000, colormap type 'viridis', font size 10, dpi 300 and display the plot on screen.



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
