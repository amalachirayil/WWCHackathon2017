from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request!"
    return render(request, 'WWCapp/index.html')

def victim(request):
    content = {
            'first_name': "sushma"

        }
    return render(request, 'WWCapp/victimpage.html', content)
