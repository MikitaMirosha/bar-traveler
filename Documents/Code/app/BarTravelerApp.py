import folium
from folium.plugins import MarkerCluster
import pandas as pd

data = pd.read_csv("pubs.txt")

number = data['NUM']
name = data['NAME']
address = data['ADDRESS']
price = data['PRICE']
latitude = data['LAT']
longitude = data['LON']


class Map(object):

    def __init__(self):
        self.number = data['NUM']
        self.name = data['NAME']
        self.address = data['ADDRESS']
        self.price = data['PRICE']
        self.latitude = data['LAT']
        self.longitude = data['LON']

    def color_change(self):
        pass


class CheapBar(Map):

    def color_change(self):
        if self.price <= 4:
            return 'green'


class MediumBar(Map):

    def color_change(self):
        if 5 <= self.price < 7:
            return 'yellow'


class LuxuryBar(Map):

    def color_change(self):
        if self.price > 7:
            return 'red'


class RightBar(Map):
    def color_change(self):
        if price <= 4:
            return 'green'
        elif 5 <= price < 7:
            return 'orange'
        else:
            return 'red'


if __name__ == "__main__":

    cheap = CheapBar()
    cheap.price = price

    medium = MediumBar()
    medium.price = price

    luxury = LuxuryBar()
    luxury.price = price

    right = RightBar()
    right.price = price

    m = folium.Map(location=[53.9000000, 27.5666700], zoom_start=12)
    m.add_child(folium.LatLngPopup())
    mc = MarkerCluster().add_to(m)

    for latitude, longitude, price, name, address in zip(latitude, longitude, price, name, address):
        folium.CircleMarker(location=[latitude, longitude], radius=9,
                            popup=str(name) + "<br>" + str(address) + "<br>" + str(price) + " BYN",
                            fill_color=right.color_change(), color="gray", fill_opacity=0.9).add_to(mc)

    m.save("pubs.html")
