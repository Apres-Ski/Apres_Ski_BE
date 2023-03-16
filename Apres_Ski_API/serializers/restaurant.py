from rest_framework import serializers

from Apres_Ski_API.models.restaurant import Restaurant

from .hour import HourSerializer
from .happyhour import HappyHourSerializer
from .photo import PhotoSerializer
from .comment import CommentSerializer
from .engagement import EngagementSerializer

class RestaurantSerializer(serializers.ModelSerializer):
  hour = HourSerializer(many=True, read_only=True)
  happyhour = HappyHourSerializer(many=True, read_only=True)
  engagement = EngagementSerializer(many=True, read_only=True)
  photo = PhotoSerializer(many=True, read_only=True)
  # comment = CommentSerializer(many=True, read_only=True)

  class Meta:
    model = Restaurant
    fields = ["id", 'name', 'address', 'food_type', 'cost', 'cover_img', 'alt_text', 'lat', 'lon', 'alcoholic_drinks', 'has_happy_hour', 'hour', 'happyhour', 'engagement', 'photo']