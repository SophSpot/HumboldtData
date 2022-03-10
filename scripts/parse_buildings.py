import json

with open('data/raw_footprints.geojson') as f:
    data = f.read()
    footprints = json.loads(data)

new_footprints_1 = {'Type': 'FeatureCollection', 'features': []}
new_footprints_2 = {'Type': 'FeatureCollection', 'features': []}
new_footprints_3 = {'Type': 'FeatureCollection', 'features': []}
new_footprints_4 = {'Type': 'FeatureCollection', 'features': []}
new_footprints_5 = {'Type': 'FeatureCollection', 'features': []}

count = 0
features = footprints.get('features')
for feature in features:
    new_feature = {'geometry': feature.get('geometry'), 'properties': {}}
    properties = feature.get('properties')
    condition = properties.get('bldg_condi')
    new_feature['bldg_condi'] = condition
    if condition == '' or condition == 'SOUND':
        new_feature['properties']['fillColor'] = '#00FF00'
    elif condition == 'NEEDS MINOR REPAIR':
        new_feature['properties']['fillColor'] = '#FFFF00'
    elif condition == 'NEEDS MAJOR REPAIR':
        new_feature['properties']['fillColor'] = '#FF0000'
    else:
        new_feature['properties']['fillColor'] = '#000000'

    if count % 5 == 0:
        new_footprints_1['features'].append(new_feature)
    if count % 5 == 1:
        new_footprints_2['features'].append(new_feature)
    if count % 5 == 2:
        new_footprints_3['features'].append(new_feature)
    if count % 5 == 3:
        new_footprints_4['features'].append(new_feature)
    if count % 5 == 4:
        new_footprints_5['features'].append(new_feature)
    count += 1






with open('data/footprints_1.geojson', 'w') as f:
    f.write(json.dumps(new_footprints_1))

with open('data/footprints_2.geojson', 'w') as f:
    f.write(json.dumps(new_footprints_2))

with open('data/footprints_3.geojson', 'w') as f:
    f.write(json.dumps(new_footprints_3))

with open('data/footprints_4.geojson', 'w') as f:
    f.write(json.dumps(new_footprints_4))

with open('data/footprints_5.geojson', 'w') as f:
    f.write(json.dumps(new_footprints_5))

# print(conditions)