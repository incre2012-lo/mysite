from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context

from .models import Person


def index(request):
    personList = Person.objects.all()

    # columnHeaders = ['First_Name', 'Last_Name', 'Salary']

    context = {
        'personList': personList,
        # 'columnHeaders': columnHeaders,
    }

    return render(request, 'index2.html', context)

def index1(request):
    return HttpResponse("This is polls 2nd view.")


def index2(request):
    # getting our template
    template = loader.get_template('index2.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(({'name': 'Rintu'})))

def index3(request):
    # getting our template
    template = loader.get_template('index3.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())
