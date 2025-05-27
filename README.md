# **🌍Where the Earth Shakes - Earthquake & Tectonic Plate Overlay Map**

A geospatial visualization of recent global earthquake activity and tectonic plate boundaries using Python and GeoPandas — plotted over a real-world basemap.

## **🚀 Features**

- **🗺️ GeoPandas-based mapping** of earthquakes and tectonic plates

- **🎯 Color-coded magnitude classes** (Moderate, High, Severe)

- **🌐 Real-world basemap overlay** with Contextily

## **🧪How to Run**

This script loads recent significant earthquakes and tectonic plate boundaries, overlays them on a basemap, and generates a high-resolution map showing where earthquakes have occurred in relation to tectonic plates.

### **🔧 Prerequisites**

Make sure the following Python libraries are installed:

geopandas
matplotlib
pandas
numpy
contextily

You can install them using:
```
pip install -r requirements.txt
```

📁 Ensure you have a PB2002_plates.json file in your data/ folder.


**1. Clone the repository**

```
git clone

https://github.com/yourusername/earthquake-tectonics-map.git
```

**2. Navigate into the Project Folder**

     cd earthquake_tectonics_map 

**3. Create a virtual environment**

python -m venv quake-env
source quake-env/bin/activate 

On Windows: quake-env\Scripts\activate 

**4. Install dependencies**

Copy code

``` pip install -r requirements.txt ```

**▶️ Running the Script**

- Open your terminal or command prompt.

- Navigate to your project directory.

- Run the following command:

python earthquake_mapping.py

**🔍 What This Script Does**

1. Loads tectonic plate boundaries from a local GeoJSON file.

2. Fetches recent significant earthquakes (past 30 days) from USGS Earthquake Feed.

3. Cleans and prepares the data:

4. Keeps only valid Point geometries with non-null magnitudes.

5. Converts earthquake time from milliseconds to human-readable datetime.

### **Categorizes earthquakes as**

🟢 Low ( < 5.0 )

🟠 Moderate ( 5.0–6.0 )

🔴 High ( > 6.0 )

- Reprojects both datasets to Web Mercator (EPSG:3857) for compatibility with basemaps.

Creates a map:

Tectonic plate boundaries in red.

Earthquake locations color-coded by magnitude.

Basemap from CartoDB Positron via Contextily.

- Saves the final map as a high-resolution PNG:

``` data/output/tectonic_plates_map.png ```

### 📂 Project Structure


earthquake-tectonics-map/
├── data/
│   ├── PB2002_plates.json
│   └── earthquake_data.csv
├── outputs/
│   └── tectonic_quakes_with_basemap.png
├── earthquake_mapping.py
├── requirements.txt
└── README.md

🛰️ Data Sources
Tectonic Plates: PB2002_plates.json

Earthquake Data: Fetched dynamically from USGS Earthquake Feed


## **🧪 Dependencies**

geopandas

pandas

matplotlib

contextily

## **📜 License**

MIT License — free to use, share, and modify!

## **🙋‍♀️ Author**

Hetvi Dharmesh Shah
📍 MSc Geoinformatics | 🌐 Remote Sensing & GIS Enthusiast
