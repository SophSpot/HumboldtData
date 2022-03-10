let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 41.906615, lng: -87.691986 },
    zoom: 17,
  });


  map.data.setStyle(function(feature) {
      var color = feature.getProperty('fillColor');
      return {
          fillColor: color,
      }
  });

  map.data.addListener('click', function(event) {
    document.getElementById('houseNumber').textContent =
      event.feature.getProperty('f_add1');
    document.getElementById('direction').textContent =
      event.feature.getProperty('pre_dir1');
    document.getElementById('streetName').textContent =
      event.feature.getProperty('st_name1');
    document.getElementById('streetType').textContent =
      event.feature.getProperty('st_type1');
    document.getElementById('buildingName').textContent =
      event.feature.getProperty('bldg_name1');
    document.getElementById('comments').textContent =
      event.feature.getProperty('comments');
    document.getElementById('editDate').textContent =
      event.feature.getProperty('edit_date');
    document.getElementById('unitNo').textContent =
      event.feature.getProperty('no_of_unit');
    document.getElementById('stories').textContent =
      event.feature.getProperty('stories');
    document.getElementById('yearBuilt').textContent =
      event.feature.getProperty('year_built');

  });

  reloadData();
}

function reloadData() {
    map.data.forEach(function(feature) {
        map.data.remove(feature);
    });
    map.data.loadGeoJson('data/footprints.geojson');
}
