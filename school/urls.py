from django.urls import path,include
from .views import (
             school_view,
             gallery_view,
             news_view,
             )

# app_name='dashboard'
urlpatterns = [
path('<slug:slug>',school_view.as_view(),name='school'),
path('gallery/<int:pk>',gallery_view.as_view(),name='gallery'),
path('news/<int:pk>',news_view.as_view(),name='news'),

]
