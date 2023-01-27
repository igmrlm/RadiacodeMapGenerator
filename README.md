# RadiacodeMapGenerator
This code uses the folium library to create a heatmap overlay of walking dose rate data on an interactive map. The data is loaded from a .rctrk file and plotted on a map centered at the mean coordinates of the data points. The heatmap is customizable with options for blur, opacity, and visibility.

# Usage
Install the folium and pandas libraries by running pip install folium pandas
Replace the file path in pd.read_csv('2023-01-22 Walking.rctrk', skiprows=1, delimiter='\t') with the file path of your own data file.
Run the script with python scriptname.py
The output file map.html will be created in the same directory, which can be opened in a web browser to view the map.
# Customization
The map's center can be changed by modifying the location parameter in folium.Map(location=[data.Latitude.mean(), data.Longitude.mean()], zoom_start=15)
The heatmap's appearance can be adjusted by modifying the parameters of the HeatMap() function, such as blur, opacity, and name.
The visibility of the heatmap can be toggled on and off using the layer control added by folium.LayerControl().add_to(m)
