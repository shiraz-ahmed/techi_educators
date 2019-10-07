from django.shortcuts import render
from django.views.generic import DetailView,UpdateView,ListView
from .models import school,news ,teacher,gallery

# Create your views here.

class school_view(DetailView):
    model=school
    template_name='school/school_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_name=school.objects.get(slug=self.kwargs['slug'])
        context['teachers']=teacher.objects.filter(school=school_name)[:4] #show the first four teachers
        context['news']=news.objects.filter(school=school_name) #show the first four teachers
        return context

# def school(request):
#     template_name='school/school_base.html'
#     return render(request,template_name)

class gallery_view(DetailView):
    model=gallery
    template_name='school/gallery.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_data=school.objects.get(id=self.kwargs['pk'])
        context['object']=school.objects.get(id=self.kwargs['pk'])
        context['object_list']=gallery.objects.filter(school=school_data)
        print("this is the context",context)
        return context

    # def get_object(self, **kwargs):
    #     school_data=school.objects.get(id=self.kwargs['pk'])
    #     s=gallery.objects.filter(school_id=school_data.id)
    #     print("this is the school i want to render ",s)
    #     return gallery.objects.filter(school_id=school_data.id)
    # def get_queryset(self):
    #     school_name=school.objects.get(slug=self.kwargs['pk'])
    #     return gallery.objects.filter(school=self.kwargs['school'])

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     school_name=school.objects.get(slug=self.kwargs['pk'])
    #     print("this is what i want to get",school_name)
    #     context['gallery']=gallery.objects.filter(school=school_name) #show the first four teachers
    #     return context

class news_view(DetailView):
    model = news
    template_name='school/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news']=news.objects.get(pk=self.kwargs['pk'])
        news_cat=news.objects.get(pk=self.kwargs['pk'])
        cat=news_cat.news_category #refers to the choice of category

        print("this is the portionn of news news_category",news_cat)
        s_id=news_cat.school.id
        context['object']=school.objects.get(pk=s_id)

        # print("this is what i want to show you for news",cat)
        context['related_news']=news.objects.filter(news_category__icontains=cat,school=s_id)
        return context
    # def get_object(self, **kwargs):
    #     # context = super().get_context_data(**kwargs)
    #     object_=news.objects.get(id=self.kwargs['pk'])
    #     return object_


# def news_view(request):
#     template_name='school/news.html'
#     return render(request,template_name)
