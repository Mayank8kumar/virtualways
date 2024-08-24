from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



# i need to change some code here
# i will make changes here


# this is a change made my gammer bhai