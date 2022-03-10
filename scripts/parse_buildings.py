import json

lower_left = (1154713.64311212,1907703.83851212)
upper_left = (1154708.44311212,1910577.63851212)
upper_right = (1160194.88156455,1910659.23266408)
lower_right = (1160436.33001804,1907776.41784924)

def main():
    with open('data/raw_footprints.geojson') as f:
        data = f.read()
        footprints = json.loads(data)

    new_footprints = {'type': 'FeatureCollection', 'features': []}

    count = 0
    features = footprints.get('features')
    for feature in features:
        new_feature = {"type": "Feature", 'geometry': feature.get('geometry'), 'properties': {}}
        properties = feature.get('properties')
        new_feature['properties'] = properties
        feature_x = float(properties.get('x_coord'))
        feature_y = float(properties.get('y_coord'))
        if not is_in_area(feature_x, feature_y):
            continue
        condition = properties.get('bldg_condi')
        if condition == '' or condition == 'SOUND':
            new_feature['properties']['fillColor'] = '#00FF00'
        elif condition == 'NEEDS MINOR REPAIR':
            new_feature['properties']['fillColor'] = '#FFFF00'
        elif condition == 'NEEDS MAJOR REPAIR':
            new_feature['properties']['fillColor'] = '#FF0000'
        else:
            new_feature['properties']['fillColor'] = '#000000'

        new_footprints['features'].append(new_feature)

    with open('data/footprints.geojson', 'w') as f:
        f.write(json.dumps(new_footprints))

def is_in_area(x, y):
    if (x > upper_left[0] and y < upper_left[1] and
        x < upper_right[0] and y < upper_right[1] and
        x > lower_left[0] and y > lower_left[1] and
        x < lower_right[0] and y > lower_right[1]):
        return True

    return False

main()