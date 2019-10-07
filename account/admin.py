from django.contrib import admin
from .models import user
#can be written as django.contrib.auth  import get_user_model

# Register your models here.
class user_manager(admin.ModelAdmin):
    list_display=['email','staff','is_active','admin']
    class Meta:
        model = user


admin.site.register(user,user_manager)
