# Mapping Pasadena Traffic Data

While teaching in Pasadena, I wanted to use some local public data. While the [City of Los Angeles](https://data.lacity.org/) had a variety of interesting, easy to use open data, it was a bit tougher to find interesting datasets on the [City of Pasadena's open data platform](https://data.cityofpasadena.net/) (though it looks like the platform and navigation has been updated since then!). I finally came upon this dataset of [traffic collisions in Pasadena](https://data.cityofpasadena.net/datasets/85f49ea583c24056968bee6e28162da4_0/explore?showTable=true).

I wanted to use this dataset with Mappa.js, but I had a problem... the coordinates weren't in a format I could use with Mappa.js. I needed latitude and longitude, and these coordinates were ESRI coordinates (specifically, ESRI 102645 (NAD 1983 StatePlane California V FIPS 0405 Feet)). I ultimately used the [pyproj module](https://pypi.org/project/pyproj/) to convert one to the other. From there, I filtered the data and wrote it to a JSON file which I then used to map the data using Mappa.js and p5.js.

![Screenshot 2024-03-27 at 11 48 18 AM](https://github.com/aiboyles/pasadena-traffic-data/assets/8883830/dc8600f5-a52f-4683-800e-c3d8c46c209a)
