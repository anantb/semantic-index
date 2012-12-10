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
		res = engine.handler.handle(sen, act)
		return HttpResponse(json.dumps(res), mimetype="application/json")
	except:
		return HttpResponse(json.dumps({'error':str(sys.exc_info())}), mimetype="application/json")
		


@csrf_exempt	
def visualize(request):
	try:
		sen = re.split('\n', request.POST['text'])
		sen = filter(lambda x: x!='' and x !='\n', sen)
		act = request.POST['action']
		out = engine.handler.handle(sen, act)
		res = {'name':act, 'children':[]}
		for event in out['events']:
			e = {'name':'', 'children':[{'name':'agents'}, {'name':'patients'}, {'name':'adverbs'}, {'name':'beneficiaries'}, {'name':'instruments'}, {'name':'time'}, {'name':'locations'}]}
			for agent in event['agents']:
				e['children'][0]['children'] = []
				a = {'name':agent['agent']}
				a['children'] = []
				for adj in event['adjectives']:
					if(agent['agent'] == adj['noun']):
						a['children'].append({'name':adj['adjective']})
				e['children'][0]['children'].append(a)
			for patient in event['patients']:
				e['children'][1]['children'] = []
				p = {'name':patient['patient']}
				p['children'] = []
				for adj in event['adjectives']:
					if(patient['patient'] == adj['noun']):
						p['children'].append({'name':adj['adjective']})
				e['children'][1]['children'].append(p)
			for adverb in event['adverbs']:
				e['children'][2]['children'] = []
				adv = {'name':adverb['adverb']}
				e['children'][2]['children'].append(adv)
			for beneficiary in event['beneficiaries']:
				e['children'][3]['children'] = []
				e['children'][3]['children'].append({'name':beneficiary['beneficiary']})
			for instrument in event['instruments']:
				e['children'][4]['children'] = []
				e['children'][5]['children'].append({'name':instrument['instrument']})
			res['children'].append(e)
   
		return HttpResponse(json.dumps(res), mimetype="application/json")
	except:
		return HttpResponse(json.dumps({'error':str(sys.exc_info())}), mimetype="application/json")