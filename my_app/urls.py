from django.urls import path
from .views import *



urlpatterns = [

	path('', IndexPageView, name='index'),
	path('center/', CenterPageView, name='center'),
	path('product/', ProductPageView, name='product'),
	path('service/', ServisePageView, name='service'),
	path('catalog/', CatalogPageView, name='catalog'),
				
]