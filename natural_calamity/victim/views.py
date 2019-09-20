from django.shortcuts import render
from .forms import Victimform


# Create your views here.
def login(request):
    if request.method == 'POST':
        print("in")
        form = Victimform(request.POST or None)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print("hellos")
    return render(request, 'victim/login.html', {})
