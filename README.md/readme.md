## Earthquake & Tectonic Plate Overlay Map

This project visualizes recent global earthquake activity along with tectonic plate boundaries using GeoPandas, overlaid on a real-world basemap. Earthquake magnitudes are color-coded to highlight intensity patterns and relationships to plate boundaries.

## Features

- *GeoPandas-based visualization* of earthquakes and tectonic plates
- *Color-coded earthquakes* by magnitude (Moderate, High, Severe)
- *Overlay on real-world basemap* using Contextily
- *Useful for *educational, geological, and spatial pattern analysis*

---

## Preview

![Map Preview](outputs/tectonic_quakes_with_basemap.png)

---

## Data Sources

- *Tectonic Plates*: [PB2002_plates.json](https://www.sciencebase.gov/catalog/item/5a2e7e87e4b0b6a76df1e8a3)
- *Earthquake Data*: Hypothetical or real dataset in data/earthquake_data.csv

---

## Folder Structure

earthquake-tectonics-map/ │ ├── data/ │   ├── PB2002_plates.json │   └── earthquake_data.csv │ ├── outputs/ │   └── tectonic_quakes_with_basemap.png │ ├── earthquake_mapping.py ├── requirements.txt └── README.md

---

## Installation

1. *Clone this repository*:

```bash
git clone https://github.com/yourusername/earthquake-tectonics-map.git
cd earthquake-tectonics-map

1. Create and activate a virtual environment (optional but recommended):

Bash

python -m venv quake-env
source quake-env/bin/activate  # On Windows: quake-env\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

---

Run the Script -

python earthquake_mapping.py

This will generate a PNG image of the map in the outputs/ folder.


---

Dependencies

geopandas

pandas

matplotlib

contextily



---

License

This project is open-source and available under the MIT License.


---

Author

Hetvi Dharmesh Shah– MSc Geoinformatics | Remote Sensing & GIS Enthusiast