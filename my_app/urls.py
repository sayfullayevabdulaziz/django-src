from django.urls import path
from .views import *



urlpatterns = [

	path('', IndexPageView, name='index'),
	path('center/', CenterPageView, name='center'),
	path('product/', ProductPageView, name='product'),
	path('service/', ServisePageView, name='service'),
	path('catalog/phonak', CatalogPageViewPhonak, name='catalog-phonak'),
	path('catalog/istok-audio', CatalogPageViewIstok, name='catalog-istok'),
				
]