from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from .models import Users, Requests, Donations

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
    print (request.session["user_id"])
    # if request.session["user_id"]:
    qs = Donations.objects.filter(donorInfo=request.session["user_id"])
    # print (qs[0].item)
    items = qs

    # items = [
    #     ["iPhone Chargers", "Electronics", "Available"],
    #     ["Walkers", "Necessity", "Available"],
    #     ["Soup Cans", "Food", "Available"],
    #     ["1 Furnished Room", "Housing", "Available"],
    # ]
    # print items
    content = {
        'user': "Sushma",
        'items': items
    }
    return render(request, 'WWCapp/donorpage.html', content)

def register(request):
    obj = Users()
    if request.method == 'POST':
        obj.username = request.POST['alias']
        obj.email = request.POST['email']
        obj.first_name = request.POST['first']
        obj.last_name = request.POST['last']
        obj.password = request.POST['password']
        obj.status = request.POST['status']
    obj.save()
    request.session['user_id']=request.POST['email']
    return redirect('/requests')

def login(request):
    # loginEmail=request.POST['email']
    request.session['user_id'] = request.POST['email']
    # qs = Donations.objects.filter(donorInfo=request.POST['email'])
    # print (qs[0].item)
    # context = {
    #     "items": qs
    # }
    return redirect('/donor')

def donateitems(request):
    return render(request, 'WWCapp/donateitems.html')

def donatesubmit(request):
    obj = Donations()
    if request.method == 'POST':
        obj.item = request.POST['item']
        obj.category = request.POST['category']
        obj.donorInfo = request.POST['contact']
        obj.status = request.POST['status']
    obj.save()
    return redirect('/donor')

# def claimed(request):
#     if request.method == 'POST':
#         user = request.POST[]

def changetoclaim(request, id):
    donateitem = Donations.objects.get(id=id)
    if donateitem.status == "Not Claimed":
        donateitem.status = "Claimed"
    elif donateitem.status == "Claimed":
        print("why")
        donateitem.status="Not Claimed"
    donateitem.save()
    return redirect('/donor')

def changetonotclaimed(request, id):
    donateitem = Donations.objects.get(id=id)
    donateitem.status = "Not Claimed"
    donateitem.save()
    return redirect('/donor')
