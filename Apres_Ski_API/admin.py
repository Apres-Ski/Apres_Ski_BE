from django.contrib import admin
from models/user import User
from models/restaurant import Restaurant
from models/hour import Hour
from models/happyhour import HappyHour
from models/photo import Photo
from models/engagement import Engagement
from models/comment import Comment
from models/lift import Lift

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Hour)
admin.site.register(HappyHour)
admin.site.register(Photo)
admin.site.register(Engagement)
admin.site.register(Comment)
admin.site.register(Lift)