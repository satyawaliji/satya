from django.shortcuts import render
from .forms import Imageform
from .models import Image
# Create your views here.
def image(request):
    if request.method=="POST":
        f=Imageform(request.POST,request.FILES)
        if f.is_valid():
            f.save()
    else:
        f=Imageform()
    i=Image.objects.all()
    return render(request,"testapp/image.html",{"form":f,"i":i})
