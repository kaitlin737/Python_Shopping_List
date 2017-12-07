from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
#from mysite.core import views as core_views
#app_name = 'shopping'
urlpatterns=[#url(r'^$',views.index, name='index'),
url(r'^$',views.Home,name='Home'),
url(r'^Shopping_List/(?P<pk>\d+)/$', views.bound_form, name='grocerylist_detail'),
url(r'^Shopping_List/saved_lists/$',views.saved_grocery_lists,name='saved_grocery_lists'),
url(r'^Shopping_List/new/$', views.grocery_new, name='grocery_new'),
url(r'^Shopping_List/(?P<pk>\d+)/edit/$', views.edit_list, name='edit_list'),

url(r'^Shopping_List/recipe/(?P<pk>\d+)/$', views.recipe_bound_form, name='recipe_detail'),
url(r'^Shopping_List/saved_recipe_list/$', views.recipe_list, name='recipe_list'),
url(r'^Shopping_List/newrecipe/$', views.add_recipe, name='add_recipe'),
url(r'^Shopping_List/(?P<pk>\d+)/recipeedit/$', views.edit_recipe, name='edit_recipe'),

url(r'^signup/$',views.signup,name='signup'),
url(r'^login/$', auth_views.login, name='login'),
url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
url(r'^delete/(?P<pk>\d+)/$', views.grocery_delete, name='grocery_delete'),
]
