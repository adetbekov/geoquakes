from django.contrib import admin
from .models import Earthquake

class EarthquakeAdmin(admin.ModelAdmin):
	model = Earthquake
	list_display = ('date','magnitude','latitude','longitude','depth')

admin.site.register(Earthquake,EarthquakeAdmin)