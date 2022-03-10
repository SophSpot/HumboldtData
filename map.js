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

  map.data.addListener('mouseover', function(event) {
    document.getElementById('issued_date').textContent =
      event.feature.getProperty('issued_date');
  document.getElementById('address').textContent =
      event.feature.getProperty('precinct') || '';
  document.getElementById('landlord').textContent =
      event.feature.getProperty('entity_or_person_s_');
  document.getElementById('violation_type').textContent =
      event.feature.getProperty('violation_type');
  });

  reloadData();

}

function reloadData() {
    map.data.forEach(function(feature) {
        map.data.remove(feature);
    });
    map.data.loadGeoJson('data/abandoned.geojson');
}
