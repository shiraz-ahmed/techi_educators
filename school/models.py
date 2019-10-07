from django.db import models
# from django.contrib.auth import get_user_model
from account.models import user
from django.utils.text import slugify
from phone_field import PhoneField
from django import forms
# Create your models here.

class school(models.Model):
    DISTRICT_CHOICES=(
    ("AB","Abbottabad"),
    ("BN","Bannu"),
    ("BG","Battagram"),
    ("CR","Charsada"),
    ("NS","Dera Ismail Khan"),
    ("HN","Hangu"),
    ("HR","Haripur"),
    ("KR","Karak"),
    ("KT","Kohat"),
    ("LK","Lower Kohistan"),
    ("MA","Mansehra"),
    ("MR","Mardan"),
    ("MM","Momand"),
    ("NS","Nowshera"),
    ("PS","Peshawar"),
    ("SB","Sawabi"),
    ("TG","Torgar"),
    ("UK","Upper Kohistan"),

    )


    user=models.ForeignKey(user,on_delete=models.CASCADE)
    school_name=models.CharField(max_length=255)
    school_short_name=models.CharField(max_length=70)
    school_email=models.EmailField(max_length=255,null=True,blank=True)
    school_contact=PhoneField(blank=True,help_text='Contact phone number')
    school_mobile=PhoneField(blank=True,help_text='Contact phone number')
    school_logo= models.ImageField(upload_to='school/school_logo/%y %m %d',null=True,blank=True)
    district=models.CharField(choices=DISTRICT_CHOICES,max_length=2)
    tehsil=models.CharField(max_length=25)

    demo_video=models.FileField(upload_to='school/videos/',null=True,blank=True)
    school_address=models.CharField(max_length=255,null=True,blank=True)
    slogan=models.CharField(max_length=50,null=True,blank=True)
    description=models.TextField(max_length=1500,null=True,blank=True)
    # for Principal
    principal_name = models.CharField(max_length=255,null=True,blank=True)
    principal_qual = models.CharField(max_length=255,null=True,blank=True)
    principal_pic = models.ImageField(upload_to='school/principal/%y %m %d',null=True,blank=True)
    principal_message = models.TextField(max_length=700,null=True,blank=True)

    #for school slider
    school_slider1 =  models.ImageField(upload_to='school/slider/%y %m %d',null=True,blank=True)
    school_slider2 =  models.ImageField(upload_to='school/slider/%y %m %d',null=True,blank=True)
    school_slider3 =  models.ImageField(upload_to='school/slider/%y %m %d',null=True,blank=True)
    school_slider_heading =models.CharField(max_length=255,null=True,blank=True)
    school_slider_desc =models.TextField(max_length=500,null=True,blank=True)



    #social links of school
    facebook_addr=models.URLField(max_length=100,null=True,blank=True)
    twitter_addr=models.URLField(max_length=100,null=True,blank=True)
    linkedin_addr=models.URLField(max_length=100,null=True,blank=True)


    #about school
    achievements=models.CharField(max_length=255,null=True,blank=True)
    teacher_expertise=models.CharField(max_length=255,null=True,blank=True)
    environment=models.CharField(max_length=255,null=True,blank=True)

    slug=models.SlugField(null=True,blank=True)


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.school_name)
        super(school,self).save(*args,**kwargs)

    def __str__(self):
        return self.school_name

class news(models.Model):
    PUBLISH_BY_CHOICES = (
        ("AD", "Admin"),
        ("SU", "Supervisor"),

    )

    CATEGORY_CHOICES=(
    ("LA","Latest"),
    ("AD","Admission"),
    ("RS","Result"),
    ("AB","About"),
    ("PR","Principal message"),
    ("OT","other"),
    )




    school=models.ForeignKey(school,on_delete=models.CASCADE)
    news_heading=models.CharField(max_length=255)
    news_desc=models.TextField(max_length=2500)
    image=models.FileField(upload_to='news/%Y %m %d/')
    timestamp=models.DateField(auto_now_add=True)
    published_by=models.CharField(choices=PUBLISH_BY_CHOICES,max_length=2)
    news_category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)

    def __str__(self):
        return self.news_heading

class teacher(models.Model):
    school=models.ForeignKey(school,on_delete=models.CASCADE)
    teacher_name=models.CharField(max_length=55)
    teacher_qual=models.CharField(max_length=255)
    teacher_intro=models.TextField(max_length=3000)
    teacher_img=models.ImageField(upload_to='teachers/%y %m %d')

    #social links of school
    facebook_addr=models.URLField(max_length=100,null=True,blank=True)
    twitter_addr=models.URLField(max_length=100,null=True,blank=True)
    gmail_id=models.URLField(max_length=100,null=True,blank=True)
    linkedin_addr=models.URLField(max_length=100,null=True,blank=True)



class gallery(models.Model):
    GALLERY_CHOICES=(
    ("LB","LAB"),
    ("CM","Classroom"),
    ("LR","Library"),
    ("CA","CAFE"),
    ("OT","Others"),)

    school=models.ForeignKey(school,on_delete=models.CASCADE)
    gallery_img_title=models.CharField(max_length=30)
    gallery_img=models.ImageField(upload_to='gallery/%y %m %d')
    img_category=models.CharField(choices=GALLERY_CHOICES,max_length=2)
