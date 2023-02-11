import pytest
import json
from django.test import TestCase, Client

class RoutingViewTests(TestCase):
  def test_routing_get(self):
    data = {
      "user_lat": 39.47677682,
      "user_lon": -106.0476996,
      "rest_lat": 39.475289,
      "rest_lon": -106.0524277
    }
    client = Client()
    response = client.get("/api/v1/routing/", data)
    content = json.loads(response.content)

    assert response.status_code == 200
    assert isinstance(content, dict)
    assert len(content) == 3
    features = content['features']
    assert isinstance(features, list)
    assert len(features) == 1
    feature = features[0]
    assert len(feature) == 3
    assert feature['type'] == 'Feature'
    assert isinstance(feature['properties'], dict)
    assert len(feature['properties']) == 7
    assert feature['properties']['mode'] == 'walk'
    assert isinstance(feature['properties']['waypoints'], list)
    assert len(feature['properties']['waypoints']) == 2
    assert feature['properties']['units'] == 'metric'
    assert feature['properties']['distance'] == 1078
    assert feature['properties']['distance_units'] == 'meters'
    assert feature['properties']['time'] == 1128.991
    assert isinstance(feature['properties']['legs'], list)
    assert len(feature['properties']['legs']) == 1
    assert isinstance(feature['properties']['legs'][0], dict)
    assert isinstance(feature['geometry'], dict)
