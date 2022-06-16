from django.shortcuts import render
from .models import trip , train
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import loginform
# Create your views here.
def index(request):
    return render(request,template_name="Home.html")

def passengerLogin(request):
    return render(request,template_name="passenger.html")




def infopassenger(request):
    trips=trip.objects.all()[:]
    return render(request,template_name="infopassenger.html" , context={"trips":trips})


def traininfo(request):
    trains=train.objects.all()[:]
    return render(request,template_name="Train.html" , context={"trains":trains})




def adminLogin(request):
    if request.method=='POST':
        print("_________________________________")
        form = loginform(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            print(password)
            print("______________________ LOGIN ___________")
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('Alogin')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'login.html',context={'form':loginform})