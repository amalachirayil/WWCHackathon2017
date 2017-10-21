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
    items = [
        ["iPhone Chargers", "Electronics", "Available"],
        ["Walkers", "Necessity", "Available"],
        ["Soup Cans", "Food", "Available"],
        ["1 Furnished Room", "Housing", "Available"],
    ]
    print items
    content = {
        'user': "Sushma",
        'items': items
    }
    return render(request, 'WWCapp/donorpage.html', content)

def register(request):
    return redirect('/requests')

def login(request):
    print request.POST
    return redirect('/donor')

def donateitems(request):
    return render(request, 'WWCapp/donateitems.html')

def donatesubmit(request):
    return redirect('/donor')
