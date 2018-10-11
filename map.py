# left to do: 
# add more entries (ended aug 19 2014) +japan 
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
      <b>%s</b> <br> %s <br> %s <br> %s
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


map = folium.Map(location=[0,0], zoom_start=3, tiles="OpenStreetMap")

fgo = folium.FeatureGroup(name="Occasions")
for lt, ln, pl, tg, d1, oc, pc in zip(lat, lon, place, tag, date1, occasion, picture):
    iframe = folium.IFrame(html=html % (str(oc), str(pl), str(d1), pc), width=250,height=200)
    fgo.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), radius=8, 
    fill=True, fill_color=color_producer(tg), fill_opacity=0.7, color='grey'))

# key - folium.FeatureGroup(name="Key")
# map.choropleth(
#     geo_data=state_geo,
#     name='choropleth',
#     data=data,
#     columns=['Tag'],
#     key_on='feature.id',
#     fill_color='YlGn',
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     legend_name='Unemployment Rate (%)'
# )



map.add_child(fgo)
# get_root().html.add_child(folium.Element(legend_html))
# map.add_child(folium.LayerControl())
map.save("Map2.html")