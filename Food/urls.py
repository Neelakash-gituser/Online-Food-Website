from django.urls import path
from . import views
urlpatterns=[

	path('',views.index,name='index'),
	path('about',views.about,name='about'),
	path('contact',views.contact,name='contact'),
	path('testimonials',views.testimonials,name='testimonials'),
	path('privacy',views.privacy,name='privacy'),
	path('achieve',views.achieve,name='achieve'),
	path('search',views.search,name='Search'),
	path('products/<int:id>',views.productview,name='Product_View'),
	path('buy',views.buy,name='buy'),

]
