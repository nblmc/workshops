import pandas as pd
import folium
from folium.plugins import MarkerCluster
from folium.vector_layers import Circle
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.distance import geodesic 

#geocoder with rate limiter for inputing multiple addresses
geolocator = Nominatim(user_agent='Brian_heatmap_assistant')
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

#get user information 
user_address = input("Please enter the address around which you'd like to search\n")
location = geocode(user_address)
radius = float(input('Please enter your desired search radius in meters:\n'))





#open data, get rid of info we don't want
crimes = pd.read_csv('data/crimes.csv', usecols = ['OFFENSE_DESCRIPTION','YEAR','MONTH','DAY_OF_WEEK','STREET','Lat','Long']).drop_duplicates()
crimes = crimes[crimes.Lat != 0]
crimes = crimes[crimes.Lat != None]
crimes = crimes.dropna(axis=0,how='any')

#limit to one year
to_check = crimes.loc[crimes['YEAR'] == 2019]




#check which ones we want to plot (look at distance compared to radius)
to_plot = []
for index, row in to_check.iterrows():
	print(row)
	if (geodesic((row['Lat'],row['Long']),(location.latitude, location.longitude))).meters <= radius:
		to_plot.append(row)

print(len(to_plot))

#map centered on user point 
map = folium.Map(location=[location.latitude, location.longitude], default_zoom_start = 13)

#circle around it 
Circle(
	location = (location.latitude, location.longitude)
	,radius = (radius)
).add_to(map)

#add markers for each incident report 
marker_cluster = MarkerCluster().add_to(map)
for item in to_plot:
	popup = 'Time:\n' + item['DAY_OF_WEEK'] + '\n' + str(item['MONTH']) + '\n' + str(item['YEAR'])
	folium.Marker(
		location = (item['Lat'], item['Long'])
		,popup = popup
		,tooltip = item['OFFENSE_DESCRIPTION']
	).add_to(marker_cluster)

#save
map.save('index.html')
