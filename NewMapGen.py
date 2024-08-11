import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from scipy.stats import gaussian_kde
import argparse

# Step 1: Parse Command-Line Arguments
parser = argparse.ArgumentParser(description='Generate an interpolated heatmap from geotagged radiation measurements.')
parser.add_argument('data_input_file', type=str, help='Path to the data input file')
parser.add_argument('--no-points', action='store_true', help='Disable plotting the data points on the heatmap')
parser.add_argument('--scale-factor', type=float, default=1.0, help='Scaling factor for density normalization')
parser.add_argument('--no-normalization', action='store_true', help='Disable normalization by density')

args = parser.parse_args()

# Step 2: Load the Data
try:
    data = pd.read_csv(args.data_input_file, sep='\t')
except FileNotFoundError:
    print(f"Error: The file {args.data_input_file} was not found.")
    exit(1)
except Exception as e:
    print(f"Error loading file: {e}")
    exit(1)

# Step 3: Process the Data
latitudes = data['Latitude']
longitudes = data['Longitude']
dose_rates = data['DoseRate']

# Step 4: Create a Grid and Interpolate the Data
grid_lat, grid_lon = np.mgrid[latitudes.min():latitudes.max():100j, longitudes.min():longitudes.max():100j]

# Interpolate the dose rates onto the grid
grid_dose_rate = griddata((latitudes, longitudes), dose_rates, (grid_lat, grid_lon), method='cubic')

# Step 5: Apply KDE for Density Estimation (if normalization is not disabled)
if not args.no_normalization:
    coords = np.vstack([latitudes, longitudes])
    kde = gaussian_kde(coords)
    density = kde(coords)
    
    # Adjust density influence with scaling factor
    adjusted_density = density ** args.scale_factor
    
    # Normalize dose rate by adjusted density
    norm_dose_rate = dose_rates / adjusted_density
else:
    norm_dose_rate = dose_rates  # Use raw dose rates if normalization is disabled

# Re-interpolate normalized (or raw) dose rates onto the grid
grid_norm_dose_rate = griddata((latitudes, longitudes), norm_dose_rate, (grid_lat, grid_lon), method='cubic')

# Step 6: Generate the Heatmap
plt.figure(figsize=(10, 8))
plt.contourf(grid_lon, grid_lat, grid_norm_dose_rate, levels=15, cmap='jet')
plt.colorbar(label='Dose Rate')

# Conditionally add the original data points
if not args.no_points:
    plt.scatter(longitudes, latitudes, c=norm_dose_rate, edgecolor='black', linewidth=1, s=50, cmap='jet')

plt.xlabel('Longitude')
plt.ylabel('Latitude')

if args.no_normalization:
    plt.title('Interpolated Heatmap of Dose Rate Measurements (Normalization disabled)')
else:
    plt.title('Normalized Interpolated Heatmap of Dose Rate Measurements')

# Save the heatmap as an image
output_file = 'interpolated_heatmap.png'
plt.savefig(output_file, dpi=300)
plt.show()

print(f"Heatmap saved to {output_file}")
