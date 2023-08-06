from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from.models import Search
from.forms import SearchForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
import folium
import geocoder
# Create your views here.
def index(request):
    # create a map
    if request.method=='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
        address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country =location.country
    if lat==None or lng==None:
        address.delete()
        return HttpResponse('Your location is not known')
    m = folium.Map(location=[0.3236, 32.5695], zoom_start=15,height="100%")
    #folium.Marker([0.3236, 32.5695],tooltip='click for more',popup='Makerere University').add_to(m)
    folium.Marker([lat, lng], tooltip='click for more', popup = country).add_to(m)
    #get html representation of a map object
    m = m._repr_html_()
    context ={
        'm': m,
        'form': form,
    }
    return render(request,'index.html',context)

'''
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid login')
            return redirect('login')
    else:   
       return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
           if User.objects.filter(username=username).exists():
               messages.info(request,'username taken')
               return redirect('register')
           elif User.objects.filter(email=email).exists():
               messages.info(request,'Email taken')
               return redirect('register')
           else:
               user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
               user.save();
               print('registered successfully')
               return redirect('login')        
        else:
           messages.info(request,'password not matching')
           return redirect('register')
        return redirect('/')
    else:

        return render(request,'register.html')
login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')
'''
