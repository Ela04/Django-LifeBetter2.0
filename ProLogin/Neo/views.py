from django.shortcuts import render

# Create your views here.

def add_user(request):
    return render(request, 'neo/adduser.html')

