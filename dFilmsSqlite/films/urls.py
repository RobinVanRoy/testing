from django.conf.urls import url
from films import views

app_name = 'films'
urlpatterns = [
    # ex: everything/  --> listview
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: everything/car/1  --> detailview
    url(r'^film/(?P<pk>[0-9]+)/$', views.FilmDetailView.as_view(), name='filmdetail'),
    # ex: everything/carbrand/1  --> detailview
    url(r'^acteur/(?P<pk>[0-9]+)/$', views.ActeurDetailView.as_view(), name='acteurdetail'),
    # ex: everything/car/create  --> createview
    url(r'^film/create/$', views.FilmCreateView.as_view(), name='filmcreate'),
    # ex: everything/carbrand/create  --> createview
    url(r'^acteur/create/$', views.ActeurCreateView.as_view(), name='acteurcreate'),
    # ex: everything/car/update  --> updateview
    url(r'^film/update/(?P<pk>[0-9]+)/$', views.FilmUpdateView.as_view(), name='filmupdate'),
    # ex: everything/car/delete/1  --> deleteview
    url(r'^film/delete/(?P<pk>[0-9]+)/$', views.FilmDeleteView.as_view(), name='filmdelete')
]
