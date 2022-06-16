from django.contrib import admin
from .models import train , trip, line ,passenger
# Register your models here.


admin.site.register(passenger)
admin.site.register(train)
admin.site.register(line)
admin.site.register(trip)
