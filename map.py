# left to do: 
# add more entries,
# change pop-up sizes by year? (hard to do with current format of date)
# add pictures to pop-up if possible


import folium
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("places.xlsx")
lat = list(data["LAT"])
lon = list(data["LON"])
tag = list(data["TAG"])
date1= list(data["DATE"])
place = list(data["PLACE"])
occasion = list(data["OCCASION"])
picture = list(data["PICTURE"])
html = """
      <b>%s</b> <br> %s <br> %s <br> <img src="%s">
"""

def color_producer(tag):
    if tag == "Relationship":
        return 'red'
    elif tag == "Event":
        return 'blue'
    elif tag == "Business":
        return 'green'
    else:
        return 'yellow'


map = folium.Map(location=[15.666678,101.018695], zoom_start=7, tiles="OpenStreetMap")

fgo = folium.FeatureGroup(name="Occasions")
for lt, ln, pl, tg, d1, oc, pc in zip(lat, lon, place, tag, date1, occasion, picture):
    iframe = folium.IFrame(html=html % (str(oc), str(pl), str(d1), str(pc)), width=175,height=100)
    fgo.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), radius=7, 
    fill=True, fill_color=color_producer(tg), fill_opacity=0.7, color='grey'))



map.add_child(fgo)
#map.add_child(fgp)
#map.add_child(folium.LayerControl())
map.save("Map2.html")