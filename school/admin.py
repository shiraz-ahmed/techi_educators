from django.contrib import admin
from .models import (
    school,news,
    teacher,gallery
    )
# Register your models here.
class school_manager(admin.ModelAdmin):
    list_display=['user','school_name','school_contact']
    class Meta:
        model = school

admin.site.register(school,school_manager)



class news_manager(admin.ModelAdmin):
    list_display=['news_heading','school','news_category','published_by']
    class Meta:
        model = news
admin.site.register(news,news_manager)



class teacher_manager(admin.ModelAdmin):
    list_display=['teacher_name','school','teacher_qual']
    class Meta:
        model = news
admin.site.register(teacher,teacher_manager)


class gallery_manager(admin.ModelAdmin):
    list_display=['school','gallery_img_title','img_category']
    class Meta:
        model = gallery
admin.site.register(gallery,gallery_manager)
