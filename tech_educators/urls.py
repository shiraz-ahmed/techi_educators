"""tech_educators URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from account.views import register,login,forgot
from django.contrib.auth.views import(
PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('forgot/',forgot,name='forgot'),
    path('school/',include('school.urls'),name='school'),
    path('dashboard/',include('dashboard.urls'),name='dashboard'),
    # path('change-password', views.change_password, name='change-password'),
    path('reset-password', PasswordResetView.as_view(template_name='account/forgot.html'), name='reset-password'),
    path('reset-password/done', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
