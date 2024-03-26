import pyproj
import csv
import json

# Define projection with Proj4 notation
# Projection definition from https://epsg.io/
esri102645=pyproj.CRS("+proj=lcc +lat_1=34.03333333333333 +lat_2=35.46666666666667 +lat_0=33.5 +lon_0=-118 +x_0=2000000 +y_0=500000.0000000002 +datum=NAD83 +units=us-ft +no_defs")
wgs84=pyproj.CRS("EPSG:4326")
# transforming from ESRI 102645 (NAD 1983 StatePlane California V FIPS 0405 Feet) to WGS84
transformer = pyproj.Transformer.from_crs(esri102645, wgs84)

# set up reading/writing to/from dictionaries
csv_file = open('Traffic_Collisions.csv', 'r')
traffic_file = open('Converted_Traffic.csv', 'w')
csv_reader = csv.DictReader(csv_file)

# define and write headers for new file
fieldnames = ['Date', 'Time', 'Day', 'Injury', 'NumberInjured', 'NumberKilled', 'Cause', 'CollisionType', 'Latitude', 'Longitude']
writer = csv.DictWriter(traffic_file, fieldnames=fieldnames)
writer.writeheader()

#set up for writing to json (if you wanna use this in a JS project)
jsonFile = open('Converted_Traffic.json', 'w')
json_data = {}

line_count = 0

for row in csv_reader:
    if line_count == 0:
        # skip the header
        line_count += 1
    elif (row["NoInjured"] != ""): # skip any blanks
      # how do you want to filter your data?
      # this grabs any accidents with more than 1 injury that
      # occurred after 2014
      if (int(row["NoInjured"]) > 1 and int(row["Date"][-2:]) > 14):
        # use pyproj to convert ESRI X Y coordinates to
        # latitude and longitude
        latlon = transformer.transform(row["X"], row["Y"])
        line_count += 1
        # write converted / pruned data to CSV file
        writer.writerow({'Date': row["Date"],
                        'Time': row["Time"],
                        'Day': row["Day"],
                        'Injury': row["Injury"],
                        'NumberInjured': row["NoInjured"],
                        'NumberKilled': row["NoKilled"],
                        'Cause': row["Cause"],
                        'CollisionType': row["CollisnTyp"],
                        'Latitude': latlon[0],
                        'Longitude': latlon[1]})
        # write to JSON file
        jsonFile.write(json.dumps({'Date': row["Date"],
                        'Time': row["Time"],
                        'Day': row["Day"],
                        'Injury': row["Injury"],
                        'NumberInjured': row["NoInjured"],
                        'NumberKilled': row["NoKilled"],
                        'Cause': row["Cause"],
                        'CollisionType': row["CollisnTyp"],
                        'Latitude': latlon[0],
                        'Longitude': latlon[1]}, indent=4))
        # separate with a comma so I can use it in
        # JS later as an array
        jsonFile.write(',')


print(f'Processed {line_count} lines')
csv_file.close()
traffic_file.close()
jsonFile.close()