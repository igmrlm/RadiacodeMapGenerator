import pandas as pd
import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='Input file name')
parser.add_argument('-a','--annotations', action='store_true', default=False, help='Enables plot annotations')
parser.add_argument('-m','--marker', action='store_true', default=False, help='Disables the circular marker')
parser.add_argument('-g','--grid_size', type=int, default=500, help='Grid size')
parser.add_argument('-c','--cmap', type=str, default='jet', help='Colormap type')
parser.add_argument('-d','--dpi', type=int, default=500, help='dpi of the saved image')
parser.add_argument('-v','--view', action='store_true', default=False, help='Enables plot.show()')
parser.add_argument('-s','--save', action='store_true', default=False, help='Enables plot.savefig()')
parser.add_argument('-f','--font_size', type=float, default=8, help='Annotation font size')

args = parser.parse_args()

data = pd.read_csv(args.file, skiprows=1, delimiter='\t')
data = data[['Latitude', 'Longitude', 'DoseRate']]
data['DoseRate'] = data['DoseRate'] * 10

grid_x = np.linspace(data['Latitude'].min(), data['Latitude'].max(), args.grid_size)
grid_y = np.linspace(data['Longitude'].min(), data['Longitude'].max(), args.grid_size)

hist, x_edges, y_edges = np.histogram2d(data['Latitude'], data['Longitude'], bins=(grid_x, grid_y), weights=data['DoseRate'])

if args.annotations:
    for i in range(len(data)):
        x = data['Longitude'].iloc[i]
        y = data['Latitude'].iloc[i]
        doserate = data['DoseRate'].iloc[i]
        plt.annotate(str(round(doserate,1)), (x, y), fontsize=args.font_size, color=plt.cm.jet(doserate/data['DoseRate'].max()))

if args.marker:
    marker = "none"
else:
    marker = "o"

plt.scatter(data['Longitude'], data['Latitude'], c=data['DoseRate'], cmap=args.cmap, marker=marker)
plt.colorbar(label="NanoSieverts per Hour")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Measured DoseRate')

if args.save:
    plt.savefig('map.png', dpi=args.dpi)
else:
    print("-s was not given so the file will not be saved to disk")
if args.view:
    plt.show()
else:
    print("-v was not given so the plot will not be shown")

print("Processing Complete")
