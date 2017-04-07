from django.conf.urls import url

from . import views

urlpatterns= [
	#url(r'^$', views.index, name='index'),
    url(r'^$', views.lBotList.as_view()),
    url(r'^a$', views.lBotList.as_view()),
	#url(r'^lchat/(?P<pk>[0-9]+)$', views.lBotDetail.as_view())
    #url(r'^lchat/bots$', views.lBotList.as_view()),
]