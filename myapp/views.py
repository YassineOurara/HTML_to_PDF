from django.shortcuts import render

# Create your views here.
import random
from django.shortcuts import redirect, render
#pre-built form utilities libraries
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse
from urllib3 import HTTPResponse
from .models import Profile
from .models import *
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from django.http import HttpResponse
from django.views.generic import View
 
#importing get_template from loader
from django.template.loader import get_template
#import render_to_pdf from util.py 
from .utils import render_to_pdf 


#hello html
def hello(request):
	return render(request,'hello.html')

#render to pdf 
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        
        #getting the template
        pdf = render_to_pdf('hello.html') #ur html page
         
         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')