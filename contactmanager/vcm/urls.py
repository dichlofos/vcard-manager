from django.conf.urls import patterns, url

from vcm import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^cards/$', views.cards, name='cards'),
)
