from django.http import JsonResponse

class MockRoutingClient():
  def get(url, data):
    if url == "/api/v1/routing/" and data == {
      "user_lat": 39.47677682,
      "user_lon": -106.0476996,
      "rest_lat": 39.475289,
      "rest_lon": -106.0524277
    }:
      response = {
        'features': [
          {
            'type': 'Feature',
            'properties': {
              'mode': 'walk',
              'waypoints': [
                {'location': [-106.047699, 39.476776], 'original_index': 0}, {'location': [-106.052427, 39.475289], 'original_index': 1}
              ],
              'units': 'metric',
              'distance': 1078,
              'distance_units': 'meters',
              'time': 1128.991,
              'legs': [
                {
                  'distance': 1078,
                  'time': 1128.991,
                  'steps': [
                    {
                      'from_index': 0,
                      'to_index': 10,
                      'distance': 87,
                      'time': 69.142,
                      'instruction': {'text': 'Walk north.'}
                    },
                    {
                      'from_index': 10,
                      'to_index': 24,
                      'distance': 602,
                      'time': 647.367,
                      'instruction': {'text': 'Turn left onto Village Road.'}
                    },
                    {
                      'from_index': 24,
                      'to_index': 34,
                      'distance': 93,
                      'time': 111.503,
                      'instruction': {'text': 'Bear right onto Kings Crown Road.'}
                    },
                    {
                      'from_index': 34,
                      'to_index': 37,
                      'distance': 85,
                      'time': 97.024,
                      'instruction': {'text': 'Turn left.'}
                    },
                    {
                      'from_index': 37,
                      'to_index': 38,
                      'distance': 26,
                      'time': 31.276,
                      'instruction': {'text': 'Turn right.'}
                    },
                    {
                      'from_index': 38,
                      'to_index': 40,
                      'distance': 99,
                      'time': 113.004,
                      'instruction': {'text': 'Turn right onto the walkway.'}
                    },
                    {
                      'from_index': 40,
                      'to_index': 41,
                      'distance': 7,
                      'time': 6.146,
                      'instruction': {'text': 'Bear right.'}
                    },
                    {
                      'from_index': 41,
                      'to_index': 46,
                      'distance': 78,
                      'time': 53.525,
                      'instruction': {'text': 'Turn right.'}
                    },
                    {
                      'from_index': 46,
                      'to_index': 46,
                      'distance': 0,
                      'time': 0,
                      'instruction': {'text': 'You have arrived at your destination.'}
                    }
                  ]
                }
              ]
            },
            'geometry': {
              'type': 'MultiLineString',
              'coordinates': [
                [
                  [-106.047704, 39.476777],
                  [-106.047723, 39.47695],
                  [-106.047742, 39.476992],
                  [-106.047775, 39.477023],
                  [-106.047828, 39.477042],
                  [-106.047927, 39.477049],
                  [-106.047972, 39.477064],
                  [-106.047996, 39.477088],
                  [-106.048033, 39.4773],
                  [-106.048059, 39.477364],
                  [-106.04809, 39.477415],
                  [-106.049076, 39.477326],
                  [-106.049285, 39.477206],
                  [-106.049527, 39.476627],
                  [-106.04979, 39.476048],
                  [-106.049899, 39.475681],
                  [-106.049848, 39.47528],
                  [-106.049903, 39.475093],
                  [-106.050068, 39.474697],
                  [-106.050157, 39.474579],
                  [-106.050313, 39.474461],
                  [-106.050501, 39.474372],
                  [-106.051612, 39.474022],
                  [-106.051751, 39.47398],
                  [-106.052137, 39.473862],
                  [-106.052222, 39.473853],
                  [-106.052326, 39.473868],
                  [-106.052433, 39.473905],
                  [-106.052515, 39.473964],
                  [-106.052586, 39.474082],
                  [-106.052617, 39.474172],
                  [-106.052636, 39.474267],
                  [-106.052615, 39.474327],
                  [-106.05257, 39.474402],
                  [-106.052527, 39.474432],
                  [-106.052747, 39.474526],
                  [-106.053144, 39.474652],
                  [-106.053423, 39.47476],
                  [-106.053427, 39.474993],
                  [-106.053116, 39.475038],
                  [-106.053213, 39.475682],
                  [-106.053168, 39.47573],
                  [-106.052988, 39.475695],
                  [-106.052734, 39.475722],
                  [-106.052508, 39.475703],
                  [-106.052414, 39.475656],
                  [-106.052323, 39.475588]
                ]
              ]
            }
          }
        ],
        'properties':
          {
            'mode': 'walk',
            'waypoints': [
              {'lat': 39.47677682, 'lon': -106.0476996},
              {'lat': 39.475289, 'lon': -106.0524277}
            ],
            'units': 'metric'
          },
        'type': 'FeatureCollection'
      }

    return JsonResponse(response)