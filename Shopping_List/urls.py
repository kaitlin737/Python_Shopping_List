from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
#from mysite.core import views as core_views

urlpatterns=[#url(r'^$',views.index, name='index'),
url(r'^$',views.Home,name='Home'),
url(r'^Shopping_List/(?P<pk>\d+)/$', views.bound_form, name='grocerylist_detail'),
url(r'^Shopping_List/saved_lists/$',views.saved_grocery_lists,name='saved_grocery_lists'),
url(r'^Shopping_List/new/$', views.grocery_new, name='grocery_new'),
url(r'^Shopping_List/(?P<pk>\d+)/edit/$', views.grocerylist_edit, name='grocerylist_edit'),
url(r'^Shopping_List/saved_recipe_list/$', views.recipe_list, name='recipe_list'),
url(r'^Shopping_List/recipe_add$', views.recipe_add, name='recipe_add'),
url(r'^signup/$',views.signup,name='signup'),
url(r'^login/$', auth_views.login, name='login'),
url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),


]
