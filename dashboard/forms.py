from django import forms
from school.models import news ,teacher,gallery

class newsform(forms.ModelForm):
    class Meta:
        model=news
        fields=['school','news_heading','news_desc','published_by','news_category','image']
        # there was issue in image uploading
        # widgets = {'school': forms.HiddenInput()}
        widgets = {
            'news_heading': forms.TextInput(attrs={'class':'form-control'}),
            'news_desc': forms.Textarea(attrs={'class':"col-lg-12"}),
            'published_by': forms.Select(attrs={'class':"form-control"}),
            'news_category': forms.Select(attrs={'class':"form-control",'id':'newscat'}),
            'school': forms.HiddenInput(),
            # 'timestamp': forms.DateField(attrs={'class':"form-control",'id':'newscat'}),
        }
        # school = forms.CharField(widget=forms.HiddenInput)


class teacherform(forms.ModelForm):
    class Meta:
        model=teacher
        fields=['school','teacher_name','teacher_qual','teacher_intro','teacher_img']
        widgets = {
            'teacher_name': forms.TextInput(attrs={'class':'form-control','required':'required'}),
            'teacher_intro': forms.Textarea(attrs={'class':"col-lg-12"}),
            'teacher_qual':forms.TextInput(attrs={'class':'form-control'}),
            'school': forms.HiddenInput(),
            # 'timestamp': forms.DateField(attrs={'class':"form-control",'id':'newscat'}),
        }



class galleryform(forms.ModelForm):
    class Meta:
        model=gallery
        fields=['school','gallery_img_title','gallery_img','img_category']
        widgets = {
            'gallery_img_title_name': forms.TextInput(attrs={'class':'form-control'}),
            'school': forms.HiddenInput(),
            # 'timestamp': forms.DateField(attrs={'class':"form-control",'id':'newscat'}),
        }
