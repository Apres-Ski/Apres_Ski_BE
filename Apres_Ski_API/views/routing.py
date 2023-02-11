import requests
from django.http import JsonResponse
from rest_framework import viewsets
from keys import routing_key

class RoutingViewSet(viewsets.ViewSet):
  def retrieve(self, request):
    params = request.GET
    response = requests.get(f"https://api.geoapify.com/v1/routing?waypoints={params['user_lat']},{params['user_lon']}|{params['rest_lat']},{params['rest_lon']}&mode=walk&apiKey={routing_key}")

    data = response.json()
    return JsonResponse(data)
