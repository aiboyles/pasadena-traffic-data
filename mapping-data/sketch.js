// Global variables to set up our map
var myMap
var canvas
// We're using Leaflet.js to set up our map
var mappa = new Mappa('Leaflet')

// this is where the map will start out:
// it will be centered on this latitude
// and longitude point, with a zoom level
// of 3 (smaller numbers means more zoomed out)
var options = {
  lat: 34.155,
  lng: -118.1309292,
  zoom: 13,
  style: "http://{s}.tile.osm.org/{z}/{x}/{y}.png"
}

function setup(){
  // We're creating our map and overlaying
  // it onto the canvas
  canvas = createCanvas(640,500)
  myMap = mappa.tileMap(options)
  myMap.overlay(canvas)
  myMap.onChange(drawTraffic)
}

function drawTraffic() {
  clear()

  strokeWeight(1)
  
  for (var i = 0; i < traffic_data.length; i++) {
    pt = myMap.latLngToPixel(traffic_data[i]["Latitude"], traffic_data[i]["Longitude"])
    // the circles will have one color if the accident occurred on
    // a weekend, and a different color if on a weekday
    if (traffic_data[i]["Day"] == "Saturday" || traffic_data[i]["Day"] == "Sunday") {
      stroke("#6c1ee8")
      fill(235, 64, 52)
    } else {
      stroke(11, 135, 69)
      fill(50, 227, 133)
    }
    ellipse(pt.x, pt.y, 5, 5)
  }
  
}

function draw(){
  
}

  