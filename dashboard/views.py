from django.shortcuts import render,HttpResponse,redirect
from school.models import school,news,teacher
from django.views.generic import ListView,DetailView,UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse
from account.models import user
from django.views.generic.edit import FormView
from .forms import newsform,teacherform,galleryform
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class dashboard(LoginRequiredMixin,DetailView):
    login_url = 'login'
    template_name='dashboard/dashboard.html'
    model = school
    #
    # def get_queryset(self,*kwargs):
    #     user = self.request.user
    #     context['object']= school.objects.get(user)
    #     return
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_name=school.objects.get(slug=self.kwargs['slug'])
        print("this is the school that i want to show",school_name)
        context['all_teachers']=teacher.objects.filter(school=school_name)
     #the same name gigs will be used in the template to access that passed on data
        return context


#
# def dashboard(request):
#     template_name='dashboard/dashboard.html'
#     return render(request,template_name)

class dashboard_gallery(LoginRequiredMixin,CreateView):
    login_url = 'login'
    form_class=galleryform
    template_name='dashboard/dashboard_gallery.html'

    def form_valid(self, form):
        # print(form.cleaned_data)
        messages.success(self.request,'Image has been added')
        return super().form_valid(form)   #super(subClass, instance).method(args)

    def form_invalid(self, form):
        print(form.errors)



    def get_success_url(self):
        return reverse('dashboard_gallery')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['object']= school.objects.get(user=user) #the same name gigs will be used in the template to access that passed on data
        return context

class dashboard_news(LoginRequiredMixin,CreateView):
    login_url = 'login'
    #model = news
    #fields=['school','news_heading','news_desc','image','timestamp','published_by','news_category']
    form_class=newsform
    template_name='dashboard/dashboard_news.html'

    # succes_url="dashboard_news"

    def form_valid(self, form):
        # print(form.cleaned_data)
        messages.success(self.request,'News has been added')
        return super().form_valid(form)   #super(subClass, instance).method(args)

    def form_invalid(self, form):
        print(form.errors)
        return HttpResponse("form is invalid.. this is just an HttpResponse object",form.errors)


    def get_success_url(self):
        return reverse('dashboard_news')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['object']= school.objects.get(user=user) #the same name gigs will be used in the template to access that passed on data
        return context




# def dashboard_news(request):
#     template_name='dashboard/dashboard_news.html'
#     return render(request,template_name)
class dashboard_user_profile(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = user
    template_name='dashboard/dashboard_profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['object']= school.objects.get(user=user) #the same name gigs will be used in the template to access that passed on data
        return context


# def dashboard_user_profile(request):
#     template_name='dashboard/dashboard_profile.html'
#     return render(request,template_name)

class dashboard_info(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = 'login'
    model = school
    template_name='dashboard/school_b_form.html'
    success_message = "school info  updated successfully"
    # fields=['']
    fields =['school_name','school_address','slogan',
    'school_contact','school_email','description',
    'demo_video','principal_name','principal_pic','principal_qual','principal_message',
    'school_slider1','school_slider2','school_slider3','school_slider_heading','school_slider_desc',
    'facebook_addr','twitter_addr','linkedin_addr',
    'achievements','teacher_expertise','environment',]

    def get_success_url(self):
        return reverse("dashboard_info",kwargs={'slug':self.kwargs['slug']})

    def form_valid(self, form):
        form.instance.user = self.request.user
        # messages.success(self.request,'school info has been updated ')
        return super().form_valid(form)   #super(subClass, instance).method(args)
    def form_invalid(self, form):
        print("these are the errrors which resists in data updating ",form.errors)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object']= school.objects.get(slug=self.kwargs['slug']) #the same name gigs will be used in the template to access that passed on data
        return context

class register_teacher(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = 'login'
    model = teacher
    template_name='dashboard/register_teacher.html'
    fields=['school','teacher_name','teacher_qual','teacher_intro','teacher_img']
    success_message="Teacher details have been added"
    # template_name='dashboard/dashboard_news'
    # succes_url="dashboard_news"

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)   #super(subClass, instance).method(args)

    # def form_invalid(self, form):
    #     print(form.errors)
    #     return HttpResponse("form is invalid.. this is just an HttpResponse object",form.errors)


    def get_success_url(self):
        return reverse('register_teacher')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['object']= school.objects.get(user=user) #the same name gigs will be used in the template to access that passed on data
        return context

# def register_teacher(request):
#     if request.method=='POST':
#         teacher_form=teacherform(request.POST)
#
#
#         if teacher_form.is_valid():
#             user_=user_form.save() #save the user into the database and keep the instance of the user to put as ForeignKey in school
#             school_=school_form.save(False) #do not post because we have to mention the user ,just collect info about school
#             school_.user=user_ #save the user into the school then after that now save
#             school_.save()
#             return redirect('login')
#         if user_form.is_valid():
#             print(school_form.errors)
#             print("user form is valide ")
#         if school_form.is_valid():
#             print(school_form.errors)
#             print("school form is valid")
#
#
#     else: #incase if the forms are not valid
#         teacher_form=userform()
#     context={
#         }
#     # context.update(csrf(request))
#     context['teacher_form']=teacher_form
#     template_name='dashboard/school_b_form.html'
#     return render(request,template_name,context)




# def dashboard_info(request):
#     template_name='dashboard/school_b_form.html'
#     return render(request,template_name)

# def dashboard_validation(LoginRequiredMixin,request):
#     login_url = 'login' #if the user is not loged in redirect him/her to login page
#     template_name='dashboard/dashboard_formvalidation.html'
#     return render(request,template_name)


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')
    # Redirect to a success page.
