from django.urls import include, path
from rest_framework import routers
from Apres_Ski_API.views.user import UserViewSet
from Apres_Ski_API.views.restaurant import RestaurantViewSet
from Apres_Ski_API.views.hour import HourViewSet
from Apres_Ski_API.views.happyhour import HappyHourViewSet
from Apres_Ski_API.views.photo import PhotoViewSet
from Apres_Ski_API.views.comment import CommentViewSet
from Apres_Ski_API.views.engagement import EngagementViewSet
from Apres_Ski_API.views.lift import LiftViewSet
# from Apres_Ski_API.views.routing import RoutingViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'restaurant', RestaurantViewSet)
router.register(r'hour', HourViewSet)
router.register(r'happy_hour', HappyHourViewSet)
router.register(r'photo', PhotoViewSet)
router.register(r'engagement', EngagementViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'lift', LiftViewSet)

urlpatterns = [
  # path('api/v1/routing/', RoutingViewSet.as_view({'get': 'retrieve'})),
  path('api/v1/', include(router.urls)),
  path('api_auth/', include('rest_framework.urls', namespace='rest_framework'))
]