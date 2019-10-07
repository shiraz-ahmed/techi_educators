from django.shortcuts import render
from school.models import school

from django.db.models import Q
# Create your views here.
def home(request):
    template_name='home/home.html'
    req=request.GET
    # dis=req.get('district')
    query=req.get('search')
    if query is not None:
        lookups = Q(school_name__icontains=query)|\
                  Q(school_short_name__icontains=query)
                  # &\ Q(district__icontains=query)
        qs = school.objects.filter(lookups).distinct()
         # mean to if both above returns the same element return only one mean distinct

    else:
        qs=school.objects.none()



    schools=school.objects.all().order_by('-id')



    context = {
        'qs': qs,
        'schools':schools
    }

    return render(request, template_name, context)
