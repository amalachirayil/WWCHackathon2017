from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
  # the index function is called when root is visited
def index(request): #signup/login
    response = "Hello, I am your first request!"
    return render(request, 'WWCapp/index.html')

def victimrequests(request):
    content = {
            'first_name': "sushma"

        }
    return render(request, 'WWCapp/victimpage.html', content)

def donations(request):

    return render(request, 'WWCapp/donorpage.html')

def register(request):
    return redirect('/requests')

def login(request):
    print request.POST
    return redirect('/donor')
