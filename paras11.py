import phonenumbers
import folium
import opencage

number=input("enter your phone number with your country code:")

from phonenumbers import geocoder
pepnumber=phonenumbers.parse(number)
location= geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode
key="c3111e227a3f41549f9d609abdc36919"
geocoder=OpenCageGeocode(key)
query=str(location)
result=geocoder.geocode(query)
lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")