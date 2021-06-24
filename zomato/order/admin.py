from django.contrib import admin
from .models import order
from .models import userregister
# Register your models here.
admin.site.register(order)
#register new site
admin.site.register(userregister)