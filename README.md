#H1-🌍 Where the Earth Shapes - Earthquake & Tectonic Plate Overlay Map


A geospatial visualization of recent global earthquake activity and tectonic plate boundaries using Python and GeoPandas — plotted over a real-world basemap.

🚀 Features
🗺️ GeoPandas-based mapping of earthquakes and tectonic plates

🎯 Color-coded magnitude classes (Moderate, High, Severe)

🌐 Real-world basemap overlay with Contextily

📚 Perfect for educational, geological, and spatial pattern analysis

📸 Preview


📂 Project Structure
arduino
Copy code
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

⚙️ Installation & Usage
1. Clone the repository
bash
Copy code
git clone https://github.com/yourusername/earthquake-tectonics-map.git
cd earthquake-tectonics-map
2. (Optional) Create a virtual environment
bash
Copy code
python -m venv quake-env
source quake-env/bin/activate  # On Windows: quake-env\Scripts\activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the script
bash
Copy code
python earthquake_mapping.py
✔️ This will generate a PNG image in the outputs/ folder.

🧪 Dependencies
geopandas

pandas

matplotlib

contextily

📜 License
MIT License — free to use, share, and modify!

🙋‍♀️ Author
Hetvi Dharmesh Shah
📍 MSc Geoinformatics | 🌐 Remote Sensing & GIS Enthusiast
