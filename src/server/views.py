from django.http import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import engine
from engine.handler import *
import json, sys, re

'''
@author: Anant Bhardwaj
@date: Nov 9, 2012
'''

def index(request):
	return render_to_response("index.html")


@csrf_exempt	
def parse(request):
	try:
		sen = re.split('\n', request.POST['text'])
		sen = filter(lambda x: x!='' and x !='\n', sen)
		act = request.POST['action']
		res = engine.handler.search(sen, act)
		return HttpResponse(json.dumps(res), mimetype="application/json")
	except:
		return HttpResponse(json.dumps({'error':str(sys.exc_info())}), mimetype="application/json")
		


@csrf_exempt	
def visualize(request):
	try:
		sen = re.split('\n', request.POST['text'])
		sen = filter(lambda x: x!='' and x !='\n', sen)
		res = engine.handler.visualize(sen)   
		return HttpResponse(json.dumps(res), mimetype="application/json")
	except:
		return HttpResponse(json.dumps({'error':str(sys.exc_info())}), mimetype="application/json")