import json

with open('data/raw_abandoned.geojson') as f:
    data = f.read()
    abandoned_buildings = json.loads(data)

with open('data/abandoned.geojson', 'w') as f:
    f.write(json.dumps(abandoned_buildings))