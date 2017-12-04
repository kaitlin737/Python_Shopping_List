from django.conf.urls import url
from . import views

urlpatterns=[#url(r'^$',views.index, name='index'),
url(r'^$',views.Home,name='Home'),
url(r'^Shopping_List/(?P<pk>\d+)/$', views.bound_form, name='grocerylist_detail'),
url(r'^Shopping_List/saved_lists/$',views.saved_grocery_lists,name='saved_grocery_lists'),
url(r'^Shopping_List/new/$', views.grocery_new, name='grocery_new'),
url(r'^Shopping_List/(?P<pk>\d+)/edit/$', views.grocerylist_edit, name='grocerylist_edit'),
#url(r'^Grocery_List/$',views.Grocery_List,name='Grocery_List'),
url(r'^Shopping_List/(?P<pk>\d+)/edit/$', views.recipe_add, name='recipe_add'),
url(r'^Shopping_List/(?P<pk>\d+)/edit/$', views.recipe_list, name='recipe_list'),
]
