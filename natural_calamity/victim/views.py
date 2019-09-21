from django.shortcuts import render

from .models import Volunteer, adminDB
from .forms import Adminform, Volunteerform, Loginform
from django.core.exceptions import ObjectDoesNotExist


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

    if (request.method == 'POST'):
        vname = request.POST.get('geoc1')
        print("hello",vname)
        all_items = Volunteer.objects.all().values()
        all_items1 = adminDB.objects.all().values()
        #print(all_items)
        loc=[]
        for i in range(len(all_items)):
            loc.append(all_items[i]['Volunteer_address'])
        for i in range(len(all_items1)):
            loc.append(all_items1[i]['address'])
        print(loc)
    return render(request, 'victim/main.html', {})


def volunteerlogin(request):
    return render(request, 'victim/volunteerlogin.html', {})

def volunteerreg(request):
    return render(request, 'victim/vol_register.html', {})

#def Volunteer1(request):
    # if request.method == 'POST':
    #   form = Volunteerform(request.POST or None)
    #  print(form.is_valid())
    # if (form.is_valid()):
    #    form.save()




def Templogin(request):
    if request.method == 'POST':
        form = Loginform(request.POST or None)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            passw = form.cleaned_data['password']
            if user=='admin' and passw=='admin123':
                return render(request, 'victim/admin.html', {})
            print(user, passw)
            all_items = Volunteer.objects.filter(Volunteer_email=user)
            all_items2=Volunteer.objects.filter(Volunteer_pass=passw)
            print(all_items[0],all_items2[0])
            if all_items[0]==all_items2[0]:
                return render(request, 'victim/volunteer.html', {'all_items':all_items})
            return render(request, 'victim/volunteerlogin.html', {})

def AdminLogin(request):
    if request.method == 'POST':
        form = Adminform(request.POST or None)
        print(form.is_valid())
        if form.is_valid():
            form.save()
    return render(request,'victim/admin.html',{})
