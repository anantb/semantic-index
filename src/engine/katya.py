from parser import *
from db import *


def getvalues(ssstanford):
	for i in sstanford:
	    if('root' in i):
	        root = i
	root = root.split(', ')
	#root = root.split('-')
	root = root[1].split('-')
	event = root[0]
	subj = ''
	subject = ''
	adverb = ''
	adjective = ''
	objec = ''
	adj= ''
	adv = ''
	subj = ''
	obj = ''
	adjRef = ''
	adjref1 = ''
	advRef = ''
	advref1 = ''
	for i in sstanford:
	    if event in i and 'nsubj' in i:
	        subj = i
	    if event in i and 'advmod' in i:
	        adv = i
	    if event in i and 'dobj' in i:
	        obj = i
	    if 'amod' in i:
	        adj = i
	if adj != '':
	    adj = adj.split(', ')
		adjref = adj.split('(')
	    adj1 = adj[1].split('-')
	    adjective = adj1[0]
		adjref1= adjref.split('-')
		adjRef = adjref1[0]			
	    if '.' in adjective:
	        adjective = adjective.split('.')[0]
	if subj != '':
	    subj = subj.split(', ')
	    subj1 = subj[1].split('-')
	    subject = subj1[0]
	    if '.' in subject:
	        subject = subject.split('.')[0]
	if adv != '':
	    adv = adv.split(', ')
		advref = adv.split(', ')
	    adv1 = adv[1].split('-')
	    adverb = adv1[0]
		advref1 = advref.split('-')
		advRef = adjref1[0]
		if advRef = event:
		
	    if '.' in adverb:
	        adverb = adverb.split('.')[0]
	if obj != '':
	    obj = obj.split(', ')
	    obj1 = obj[1].split('-')
	    objec = obj1[0]
	    if '.' in objec:
	        objec = objec.split('.')[0]
	if event = '':
		event = None
	if adjective = '':
		event = None
		adjRef = None
	if adverb = '':
		adverb = None
		advRef = None
	if obj = '':
		obj = None
		

	if adjRef == object:
		if advRef == event:
			out = dict('event':[event,adverb], 'subject':[subject], 'object':[obj, adjective])
		else:
			out = dict('event':[event], 'subject':[subject], 'object':[obj, adjective])
	else if adjRef == subject:
		if advRef == event:
			out = dict('event':[event,adverb], 'subject':[subject, adjective], 'object':[obj])
		else:
			out = dict('event':[event], 'subject':[subject, adjective], 'object':[obj])
	else:
		if advRef == event:
			out = dict('event':[event,adverb], 'subject':[subject], 'object':[obj])
		else:
			out = dict('event':[event], 'subject':[subject], 'object':[obj])
	return out	


stanford = stanford_parse_local('Blue Max plays tennis well.')
sstanford = stanford.split('),')
e = EventInstance()
sentence = getvalues(sstanford)
if(len(sentence.get('event')) == 1):
	action = e.insert_action(sentence.get('event')[0])
if(len(sentence.get('event')) == 2):
	action = e.insert_action(sentence.get('event')[0])
	adve = e.insert_adverb(sentence.get('event')[1], action)
if(len(sentence.get('subject')) == 1):
	agent1 = e.insert_agent(sentence.get('subject')[0])
if(len(sentence.get('subject')) == 2):
	agent1 = e.insert_agent(sentence.get('subject')[0])
	adje1 = e.insert_adjective(sentence.get('subject')[1], agent1)
if(len(sentence.get('object')) == 1):
	patient = e.insert_patient(sentence.get('object')[0])
if(len(sentence.get('object')) == 2):
	patient = e.insert_patient(sentence.get('object')[0])
	adje1 = e.insert_adjective(sentence.get('object')[1], patient)

#instrument = e.insert_instrument('with a knife', action)
#time = e.insert_time('on 5 pm', action)
#location = e.insert_location('at Stata Center', action)


q = EventQuery()
res = q.search_action('plays')
print res
		

print subject + ' ' + event + ' ' + objec + ' ' + adjective + ' ' + adverb
 