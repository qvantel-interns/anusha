from django.shortcuts import render
from .forms import *

def Sign(request):
    form = SignUpForm(request.POST or None)
    form.save()
  
    return render(request,"signups/sample.html",{"form":form})
