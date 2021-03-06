from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from sellbuy.models import ShareDetail
from .models import UserDetail
from importlib import import_module
from django.core.urlresolvers import clear_url_caches
from django.db import models
from django.apps import apps
from django.contrib import admin
from django.conf import settings
#from portfolio.models import User_transact
#from portfolio import views_portfolio as vp# import Matrixr,Matrix
import numpy as np
@csrf_protect
def login_check(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    else:
        return HttpResponseRedirect('/login')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        no = ShareDetail.objects.count()
        if no == None:
            number= 1
        else:
            number= no + 1
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            sharedetail=ShareDetail.objects.create(
            username=form.cleaned_data['username'],
            id=number
                )
            #user_transact=User_transact.objects.create(
            #username=form.cleaned_data['username'],
            #    )
            userdetail=UserDetail.objects.create(
            name=form.cleaned_data['username'],
            id=number,
            email=form.cleaned_data['email'],
            branch=form.cleaned_data['branch'],
            college=form.cleaned_data['college'],
            contact=form.cleaned_data['contact'],
                )
            #global Matrix,Matrixr
            
            file_data = np.loadtxt('portfolio.csv', delimiter=' ',dtype='str')
            Matrix=file_data
            f = open ( 'portfolio_dim_r.txt')
            for row in f:
                Matrixr =int(row)
            f = open ( 'portfolio_dim_c.txt')
            for col in f:
                Matrixc=int(col)
            Matrix[Matrixr][0] = form.cleaned_data['username']
            Matrixr+=1
            np.savetxt("portfolio.csv",Matrix,fmt='%s')
            with open('portfolio_dim_r.txt', 'w') as f:
                f.write(str(Matrixr))
            with open('portfolio_dim_c.txt', 'w') as f:
                f.write(str(Matrixc))
            return HttpResponseRedirect('/success/')
    

    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def registersuccess(request):
    return render_to_response(
        'registration/success.html',
        )

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

flag=0

@login_required
def home(request):
    user = UserDetail.objects.get(name=request.user)
    name = user.name
    return HttpResponseRedirect('/transact')
    return render_to_response(
        'sellbuy/transact.html',
        {'name': name}
        )

def start(request):
    from django.core import management
    return render_to_response(
        'start.html',
        )