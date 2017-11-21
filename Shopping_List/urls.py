from django.conf.urls import url
from . import views

urlpatterns=[#url(r'^$',views.index, name='index'),
url(r'^$',views.saved_grocery_lists,name='saved_grocery_lists'),
#url(r'^Grocery_List/$',views.Grocery_List,name='Grocery_List'),
]
