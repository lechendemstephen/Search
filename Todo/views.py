from django.shortcuts import render
from django.db.models import Q

from django.contrib import messages 
from .models import Students
# Create your views here.


def home(request):
    student = Students.objects.all()

    context = {
        'students': student
    }
    return render(request, 'todo/pages/home.html', context )


def search_student(request): 
    student = Students.objects.all()

    if request.method == "POST": 
        # getting the search quuery from the user using standard Django forms
        search_query = request.POST['search_query']
        # writing result of the search quarell based on search input 
        result = Students.objects.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))   
        context = {
            'query': search_query,
            'students': student,
            'results':result
        }

        return render(request, 'todo/pages/home.html', context ) 
     
    else: 
      pass 