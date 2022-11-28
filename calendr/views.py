from django.shortcuts import render
from .helpers import *

# Create your views here.
def index(request):
    
    return render(request, 'calendr/calendar.html')

