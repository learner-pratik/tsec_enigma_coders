from django.shortcuts import render
from .forms import Adminform, Volunteerform


# Create your views here.
def login(request):
    if request.method == 'POST':
        print("in")
        form = Adminform(request.POST or None)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print("hellos")
    return render(request, 'victim/admin.html', {})

def addVolunteer(request):
    if request.method == 'POST':
        form = Volunteerform(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request, 'victim/volunteersignup.html', {})

def home(request):
    return render(request, 'victim/main.html', {})


