from django.urls import path
from .views import IndexPageView, CenterPageView, ProductPageView, ServisePageView, \
                   CatalogPageView, NewsPage, center_tashkent, center_tashkent2



urlpatterns = [

	path('', IndexPageView, name='index'),
	path('center/', CenterPageView, name='center'),
	path('product/<slug:slug>', ProductPageView, name='product'),
	path('service/', ServisePageView, name='service'),
	# path('catalog/phonak', CatalogPageViewPhonak, name='catalog-phonak'),
	path('catalog/<slug:slug>', CatalogPageView, name='catalog-product'),
	path('news/<slug:slug>', NewsPage, name='news'),
	path('centers/respublika_uzbekistan/tashkent/', center_tashkent, name='center_tashkent'),
	path('centers/respublika_uzbekistan/tashkent-2/', center_tashkent2, name='center_tashkent2'),

]