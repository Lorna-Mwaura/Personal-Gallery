from django.shortcuts import render
from .models import Image

# Create your views here.
def welcome(request):

    image = Image.objects.all()
    ctx = {'image':image}
    return render(request,'index.html', ctx)