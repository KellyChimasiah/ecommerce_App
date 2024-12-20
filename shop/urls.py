from django.urls import path
from shop import views

urlpatterns=[
    path('',views.item_view, name='item_view')
] 