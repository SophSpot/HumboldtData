let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 41.8781, lng: -87.6298 },
    zoom: 10,
  });


  map.data.setStyle(function(feature) {
      var color = feature.getProperty('fillColor');
      return {
          fillColor: color,
      }
  });
  
  reloadData();
}

function reloadData() {
    map.data.forEach(function(feature) {
        map.data.remove(feature);
    });
    map.data.loadGeoJson('abandoned.geojson');
}
