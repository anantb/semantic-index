import httplib, urllib, subprocess
if __name__ == "__main__":
	p = os.path.abspath(os.path.dirname(__file__))
	if(os.path.abspath(p+"/..") not in sys.path):
		sys.path.append(os.path.abspath(p+"/.."))
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

from server.models import *


def parse(params, url='/parser/parser.jsp'):
	conn = httplib.HTTPConnection("anantb.csail.mit.edu:8080")
	headers = {"Content-type": "application/x-www-form-urlencoded",
			"Accept": "text/plain"}
	params = urllib.urlencode(params)
	conn.request("POST", url, params, headers)	
	res = conn.getresponse().read()
	return res


def parse_local(sen):
	subprocess.call(["ls", "-l"])
	

def test_db():
	action = 'loves'
	subj = 'John'
	obj = 'nlp'

	e = Event()
	e.save()
	act = None
	sub = None
	obj = None

	try:
		act = Action.objects.get (name = 'loves')
	except Action.DoesNotExist:
		act = Action(name='loves')
		act.save()
	
	try:
		obj = Noun.objects.get (name = 'nlp')
	except Noun.DoesNotExist:
		obj = Noun(name='nlp')
		obj.save()
	
	
	try:
		sub = Noun.objects.get (name = 'John')
	except Noun.DoesNotExist:
		sub = Noun(name='John')
		sub.save()
	



	ea = EventAction(action = act, event = e)
	ea.save()

	esubj = EventAgent(agent = sub, event = e)
	esubj.save()

	ep = EventPatient(patient = obj, event = e)
	ep.save()




	a = Action.objects.get(name='loves')
	event_actions = EventAction.objects.filter(action = a)
	agents = []
	patients = []
	for e.event in event_actions:
		agents.append({'event': e.event.id, 'agents': [ea.agent.name for ea in EventAgent.objects.filter(event = e)]})
		patients.append({'event': e.event.id, 'patients': [ep.patient.name for ep in EventPatient.objects.filter(event = e)]})

	print agents
	print patients 
	
	