import geopandas as gpd
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
from datetime import datetime
import contextily as ctx

try:
    #Load tectonic plate boundaries
    data_dir = r"C:\Users\91966\Desktop\Projects\earthquake-mapping-geopandas\data"
    plates = gpd.read_file(os.path.join(data_dir, "PB2002_plates.json"))
    plates = plates.to_crs(epsg=3857)  # Reproject plates to Web Mercator

    #Define the URL for recent earthquakes (last 30 days)
    earthquake_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"

    #Load earthquake data as GeoDataFrame
    earthquakes = gpd.read_file(earthquake_url)
    earthquakes = earthquakes.to_crs(epsg=3857)  # Reproject earthquakes to Web Mercator

    #Filter only earthquakes with location points and valid magnitudes
    earthquakes = earthquakes[earthquakes.geometry.type == "Point"]
    earthquakes = earthquakes.dropna(subset=['mag'])  # Remove rows with missing magnitudes

    # Convert time from milliseconds to datetime
    earthquakes['time'] = pd.to_datetime(earthquakes['time'], unit='ms')

    # Categorize earthquakes based on magnitude
    def categorize_magnitude(mag):
        if mag < 5.0:
            return "Low"
        elif mag < 6.0:
            return "Moderate"
        else:
            return "High"

    earthquakes["category"] = earthquakes["mag"].apply(categorize_magnitude)

    print("Earthquake data loaded:")
    print("\nDataset Information:")
    print(f"Number of earthquakes: {len(earthquakes)}")
    print(f"Magnitude range: {earthquakes['mag'].min():.1f} to {earthquakes['mag'].max():.1f}")
    print("\nRecent earthquakes:")
    print(earthquakes[["place","mag","category","time"]].head())

    # Create figure and axis with specific size
    fig, ax = plt.subplots(figsize=(15, 10))

    # Plot tectonic plates first
    plates.boundary.plot(ax=ax, color='red', linewidth=1, label='Tectonic Plates', alpha=0.7)

    # Plot earthquakes
    color_map = {"Low": "green", "Moderate": "orange", "High": "red"}
    for category in sorted(earthquakes["category"].unique()):
        subset = earthquakes[earthquakes["category"] == category]
        color = color_map.get(category, "blue")
        subset.plot(
            ax=ax,
            markersize=subset["mag"] * 30,  # Reduced marker size
            color=color,
            label=f"{category} Magnitude",
            alpha=0.6
        )

    # Set reasonable bounds for the map (in Web Mercator coordinates)
    ax.set_xlim(-18000000, 18000000)
    ax.set_ylim(-8000000, 8000000)

    # Add basemap with appropriate zoom level
    ctx.add_basemap(
        ax,
        source=ctx.providers.CartoDB.Positron,  # Using a different basemap provider
        zoom=2
    )

    # Customize the appearance
    ax.set_title("Global Tectonic Plate Boundaries and Recent Significant Earthquakes",
                fontsize=16, pad=20)
    ax.legend(fontsize=10, loc='upper right', bbox_to_anchor=(1.15, 1))
    ax.set_axis_off()

    # Save the map with tight layout
    output_dir = os.path.join(data_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, "tectonic_plates_map.png"), 
                dpi=300, 
                bbox_inches='tight',
                pad_inches=0.5)
    plt.show()

except Exception as e:
    print(f"An error occurred: {str(e)}")
    if 'plates' in locals():
        print("\nPlates CRS:", plates.crs)
    if 'earthquakes' in locals():
        print("Earthquakes CRS:", earthquakes.crs)

