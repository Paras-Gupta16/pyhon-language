# See our full Python tutorial:
# https://opencagedata.com/tutorials/geocode-in-python

from opencage.geocoder import OpenCageGeocode

OCG = OpenCageGeocode('c3111e227a3f41549f9d609abdc36919')
results = OCG.reverse_geocode(14.666, 76.833)
print(results[0]['formatted'])
# Sirigedoddi, Gummagatta, India

results = OCG.geocode(u'Athens')
print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'],
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))
# 37.983941;23.728305;gr;Europe/Athens

results = OCG.geocode(u'Athens, Texas', language='de')
print(results[0]['components']['country'])
# Vereinigte Staaten von Amerika