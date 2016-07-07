from django.http import HttpResponse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *
from sellbuy .models import *
from django.db import models
from django.apps import apps
from django.contrib import admin
from django.conf import settings
from importlib import import_module
from .models import *
from .admin import *
from django.core.urlresolvers import clear_url_caches
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from sellbuy.models import Share, ShareDetail,Timer,News
def graph(request,name):

	mymodel=apps.get_model('portfolio',name)

	query_x = mymodel.objects.values_list('x')
	query_y = mymodel.objects.values_list('y')
	plt.plot(query_x,query_y)

	response = HttpResponse(content_type='image/png')
	# create your image as usual, e.g. pylab.plot(...)
	plt.savefig(response, format="png")
	plt.close()
	
	return response

i = 0

Matrix = [['0' for x in range(1000)] for y in range(100)]
Matrixc = 1
Matrixr = 0
for o in ShareDetail.objects.all():
	Matrix[Matrixr][0]=o.username
	Matrixr+=1

@login_required
def portfolio(request):
	#dataimg='<img style="-webkit-user-select: none; cursor: zoom-in;" src="./graph/'+request.user+'"width="147" height="110">'
	#dict={data:da}
	return render_to_response(
		'portfolio/portfolio.html',{'name':request.user})

def fetch_portfolio_graph(request):
	global Matrixr,Matrix,Matrixc
	y_array = [float(0) for x in range(0,Matrixc-1)]
	for x in range(0,Matrixr):
		if(str(Matrix[x][0])==str(request.user)):
			for col in range(1,Matrixc):
				y_array[col-1]=Matrix[x][col]
	
	x_array = [x for x in range(0,Matrixc-1)]
	print x_array
	print y_array
	plt.plot(x_array,y_array)
	response = HttpResponse(content_type='image/png')
	plt.savefig(response, format="png")
	plt.close()
	return response
def leader_board(request):
	
	return response