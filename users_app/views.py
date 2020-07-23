from django.shortcuts import render, redirect
from .models import Users
# Create your views here.


def get_users(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'index.html', context)


def add_users(request):
    Users.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email_address=request.POST['email_address'],
        age=int(request.POST['age'])
    )
    return redirect('/')
