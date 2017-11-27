from django.conf.urls import url
from . import views

urlpatterns=[#url(r'^$',views.index, name='index'),
url(r'^Shopping_List/(?P<pk>\d+)/$', views.grocery_detail, name='grocery_detail'),
url(r'^$',views.saved_grocery_lists,name='saved_grocery_lists'),
url(r'^Shopping_List/new/$', views.grocerylist_new, name='grocerylist_new'),
#url(r'^Grocery_List/$',views.Grocery_List,name='Grocery_List'),
]
