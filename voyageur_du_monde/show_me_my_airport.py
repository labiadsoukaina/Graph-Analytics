import folium
import pandas as pd

airports = pd.read_csv("airports.csv")
airports_df = pd.DataFrame(airports)
# airports_df.head()

def show_me_my_airport(my_airport):
    loc = return_location(my_airport)
    map = folium.Map(location=loc)
    map.save(my_airport+".html")


def return_location(airport_name):
    location = []
    airport = airports_df[airports_df['Name'] == airport_name]
    lat = airport.iloc[0]['Latitude']
    long = airport.iloc[0]['Longitude']
    location.append(lat)
    location.append(long)
    return location

show_me_my_airport("Toulouse-Blagnac Airport")