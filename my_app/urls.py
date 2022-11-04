from django.urls import path
from .views import *



urlpatterns = [

	path('', IndexPageView, name='index'),
	path('center/', CenterPageView, name='center'),
	path('product/<slug:slug>', ProductPageView, name='product'),
	path('service/', ServisePageView, name='service'),
	# path('catalog/phonak', CatalogPageViewPhonak, name='catalog-phonak'),
	path('catalog/<slug:slug>', CatalogPageView, name='catalog-product'),
	path('news/<slug:slug>', NewsPage, name='news')
]