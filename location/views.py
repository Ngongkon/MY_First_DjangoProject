from django.shortcuts import render
from .models import College
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.
'''
def map(request):
    colleges = College.objects.all()
    return render(request, 'map.html', {'colleges': colleges})
'''
@login_required(login_url='login')
def map(request):
    context = {
        'api_key': 'settings.GOOGLE_MAPS_API_KEY'
    }
    return render(request, 'map.html', context)

