from django.contrib import admin
from Apres_Ski_API.models.user import User
from Apres_Ski_API.models.restaurant import Restaurant
from Apres_Ski_API.models.hour import Hour
from Apres_Ski_API.models.happyhour import HappyHour
from Apres_Ski_API.models.photo import Photo
from Apres_Ski_API.models.engagement import Engagement
from Apres_Ski_API.models.comment import Comment
from Apres_Ski_API.models.lift import Lift

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Hour)
admin.site.register(HappyHour)
admin.site.register(Photo)
admin.site.register(Engagement)
admin.site.register(Comment)
admin.site.register(Lift)