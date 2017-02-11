from django.conf.urls import url,include
from studybank import views
urlpatterns = [
	url(r'$', views.index, name='index')
]