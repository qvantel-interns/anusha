from django.shortcuts import render,render_to_response,RequestContext
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
def index(request):
    context=RequestContext(request)
    return render(request,"bsstest/index.html",context)

def bsstest(request):
    form = bsstestForm(request.POST or None)
    if form.is_valid():
	form.save()
  
    return render(request,"bss.html",{"form":form})

def register(request):
    context = RequestContext(request)
    registered = False

    
    if request.method == 'POST':
        
        user_form = UserForm(data=request.POST)
       

        if user_form.is_valid():
            
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()
        
   
    return render_to_response(
            'bsstest/register.html',
            {'user_form': user_form, 'registered': registered},
            context)


def user_login(request):
    
    context = RequestContext(request)

    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
		print "a"
                return HttpResponseRedirect('/bsstest/')
            else:
                return HttpResponse("Your bsstest account is disabled.")
        else:
           
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    
    else:
        print "b"
        return render_to_response('bsstest/login.html', {}, context)
