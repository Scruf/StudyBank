from django.conf.urls import url,include
from studybank import views
urlpatterns = [
	url(r'^student/$', views.user_list),
	url(r'^$',views.index)
]