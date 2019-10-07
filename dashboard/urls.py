from django.urls import path,include
from .views import (
             dashboard,
             dashboard_gallery,
             dashboard_news,
             dashboard_user_profile,
             dashboard_info,
             # dashboard_validation,
            register_teacher,
            logout_view,
             )

# app_name='dashboard'
urlpatterns = [
path('<slug:slug>',dashboard.as_view(),name='dashboard_home'),
path('dashboard_gallery/',dashboard_gallery.as_view(),name='dashboard_gallery'),
path('dashboard_news/',dashboard_news.as_view(),name='dashboard_news'),
path('dashboard_profile/<int:pk>',dashboard_user_profile.as_view(),name='dashboard_user_profile'),
# path('update/<int:pk>',update_gig.as_view(), name='update_gig'),
path('dashboard_info/<slug:slug>',dashboard_info.as_view(),name='dashboard_info'),
# path('dashboard_validation/',dashboard_validation,name='dashboard_validation'),
path('register_teacher/',register_teacher.as_view(),name='register_teacher'),
path('logout/',logout_view,name='logout'),

]
