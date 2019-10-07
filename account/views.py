from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login # this is because the two have the same name
# from .models import user
from django.views.generic import ListView,DetailView,UpdateView,CreateView
from school.models import school
from .models import user
from .forms import schoolform,userform
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

# class register(CreateView):
#     model=user
#     fields=['name','email','password']
#     template_name='account/register.html'
#
#     def form_valid(self, form):
#         # print(form.cleaned_data)
#         return super().form_valid(form)   #super(subClass, instance).method(args)
#
#     def form_invalid(self, form):
#         print(form.errors)
#         return HttpResponse("form is invalid.. this is just an HttpResponse object",form.errors)

# def school_register(CreateView):
#     model=school
#     fields=[]
#     def form_valid(self, form):
#         # print(form.cleaned_data)
#         return super().form_valid(form)   #super(subClass, instance).method(args)
#
#     def form_invalid(self, form):
#         print(form.errors)
#         return HttpResponse("form is invalid.. this is just an HttpResponse object",form.errors)

def register(request):
    if request.method=='POST':
        user_form=userform(request.POST)
        school_form=schoolform(request.POST)

        if user_form.is_valid() and school_form.is_valid():
            # messages.success(request,'you have been registered')
            user_=user_form.save() #save the user into the database and keep the instance of the user to put as ForeignKey in school
            school_=school_form.save(False) #do not post because we have to mention the user ,just collect info about school
            school_.user=user_ #save the user into the school then after that now save
            messages.success(request,"Account has been created")
            school_.save()
            return redirect('login')
        if user_form.is_valid():
            print(school_form.errors)
            print("user form is valide ")
        if school_form.is_valid():
            print(school_form.errors)
            print("school form is valid")


    else: #incase if the forms are not valid
        user_form=userform()
        school_form=schoolform()
    context={
        }
    # context.update(csrf(request))
    context['user_form']=user_form
    context['school_form']=school_form
    template_name='account/register.html'
    return render(request,template_name,context)



def login(request):
    if request.method == 'POST':
        useremail = request.POST['email'] # get the name which is  entered by the user,must have the same name as in the form
        password = request.POST['pass'] # get password
        print(useremail,password)
        user=authenticate(request, username=useremail, password=password) #match the name password with database
        if user is not None:
            user_login(request, user)
            school_= school.objects.get(user=request.user)
            remove_=useremail.replace('@','') #find email address and replace . with ''
            slug_=remove_.replace('.','')
            #test= mail.find('.') print(test) balance=mail[0:test]+mail[test+1:] print(balance) this method can also be used
            print("user is  verified")
            return redirect('dashboard_home' ,slug=school_.slug) # redirect to the home page
            # context['login_f'] = login_form()
        else:
            # raise ValidationError('check your Email or Password')
            return redirect('login')
            print("user is not verified")

    template_name='account/login.html'
    return render(request,template_name)


def forgot(request):
    template_name='account/forgot.html'
    return render(request,template_name)
