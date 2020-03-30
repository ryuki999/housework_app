from django.contrib import admin
from .models import User,Housework,Workreport,Day_rank

# Register your models here.
admin.site.register(User)
admin.site.register(Housework)
admin.site.register(Workreport)
admin.site.register(Day_rank)