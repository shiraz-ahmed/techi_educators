from django import forms
from school.models import school
from account.models import user

class userform(forms.ModelForm):
    class Meta:
        model=user
        fields=['name','email','password']
        widgets={
        'name': forms.TextInput(attrs={'class':'form-control','placeholder':"Username",'id':'username'}),
        'email': forms.EmailInput(attrs={'class':'form-control','placeholder':"Your Email",'id':'email'}),
        'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':"Password",'id':'password','minlength':8}),
        }
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(userform, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean_email(self):
        email=self.cleaned_data.get('email')
        query = user.objects.filter(email=email)
        if query.exists():
            raise forms.ValidationError("email address has already been taken try another")
        return email




class schoolform(forms.ModelForm):
    class Meta:
        model=school
        fields=['school_name','school_short_name','school_address','school_contact','school_mobile','district','tehsil']

        widgets={
        'school_name': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Complete School Name",'id':'schlnme','required':'required'}),
        'school_short_name': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter School Short Name",'id':'shortname'}),
        'school_address': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter School Address",'id':'address','required':'required'}),
        'school_contact': forms.NumberInput(attrs={'class':'form-control','placeholder':"Enter contact no",'id':"contactno" ,'name':"contactno"}),
        'school_mobile': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Phone Number",'id':'phnno','name':"mobno"}),
        'district': forms.Select(attrs={'class':'form-control','id':'district'}),
        'tehsil': forms.TextInput(attrs={'class':'form-control','id':'tehsil'}),


        }
