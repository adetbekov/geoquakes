from django.conf.urls import url
import geo.views

urlpatterns = [
    url(r'^$', geo.views.index, name="map"),
    url(r'^charts/magnitude$', geo.views.magchart, name="magchart"),
    url(r'^charts/frequency$', geo.views.freqchart, name="freqchart"),
]