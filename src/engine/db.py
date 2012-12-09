import  os, sys, subprocess
if __name__ == "__main__":
	p = os.path.abspath(os.path.dirname(__file__))
	if(os.path.abspath(p+"/..") not in sys.path):
		sys.path.append(os.path.abspath(p+"/.."))
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
from server.models import *


'''
@author: anant bhardwaj
@date: Dec 8, 2012

Actual Schema

'''
class EventInstance:
	def __init__(self):
		self.e = Event()
		self.e.save()
	
	
	def insert_action(self, action):
		_action = None
		try:
			_action = Action.objects.get(name = action)
		except Action.DoesNotExist:
			_action = Action(name= action)
			_action.save()
		_eaction = EventAction(action = _action, event = self.e)
		_eaction.save()
		return _action
	
		
	def insert_agent(self, agent):
		_agent = agent
		try:
			_agent = Noun.objects.get(name = agent)
		except Noun.DoesNotExist:
			_agent = Noun(name=agent)
			_agent.save()
		_eagent = EventAgent(agent = _agent, event = self.e)
		_eagent.save()
		return _agent
	
	
	
	def insert_patient(self, patient):
		_patient = None
		try:
			_patient = Noun.objects.get(name = patient)
		except Noun.DoesNotExist:
			_patient = Noun(name= patient)
			_patient.save()
		_epatient = EventPatient(patient = _patient, event = self.e)
		_epatient.save()
		return _patient
		
	
	
	def insert_beneficiary(self, beneficiary):
		_beneficiary = None
		try:
			_beneficiary = Noun.objects.get(name = beneficiary)
		except Noun.DoesNotExist:
			_beneficiary = Noun(name= beneficiary)
			_beneficiary.save()
		_ebeneficiary = EventBenificiary(beneficiary = _beneficiary, event = self.e)
		_ebeneficiary.save()
		return _beneficiary
		
	
	
	def insert_instrument(self, instrument):
		_instrument = None
		try:
			_instrument = Noun.objects.get(name = instrument)
		except Noun.DoesNotExist:
			_instrument = Noun(name= instrument)
			_instrument.save()
		_einstrument = EventInstrument(instrument = _instrument, event = self.e)
		_einstrument.save()
		return _instrument
		
	
	
	def insert_location(self, location):
		_location = None
		try:
			_location = Noun.objects.get(name = location)
		except Noun.DoesNotExist:
			_location = Noun(name= location)
			_location.save()
		_elocation = EventLocation(location = _location, event = self.e)
		_elocation.save()
		return _location
	
	
	
	
		
	def insert_time(self, time):
		_time = None
		try:
			_time = Noun.objects.get(name = time)
		except Noun.DoesNotExist:
			_time = Noun(name= time)
			_time.save()
		_elocation = EventTime(time = _time, event = e)
		_elocation.save()
		return _time
	
	
	
	
	def insert_adjective(self, adjective, noun):
		_adjective = None
		try:
			_adjective = Adjective.objects.get(name = adjective)
		except Adjective.DoesNotExist:
			_adjective = Adjective(name= adjective)
			_adjective.save()
		_eadjective = EventAdjective(adjective = _adjective, action = action, event = self.e)
		_eadjective.save()
		
	
	
	
	def insert_adverb(self, adverb, action):
		_adverb = None
		try:
			_adverb = Adverb.objects.get(name = adverb)
		except Adverb.DoesNotExist:
			_adverb = Adverb(name= adverb)
			_adverb.save()
		_eadverb = EventAdverb(adverb = _adverb, action = action, event = self.e)
		_eadverb.save()
	
		
		
		


class EventQuery:
	def __init__(self):
		self.event = None
	
	def search_action(self, action):
		res = {}
		action = Action.objects.get(name=action)	
		event_actions = EventAction.objects.filter(action = action)
		res['events']=[]
		for e in event_actions:
			event = {}
			event['id'] = e.event_id
			event['agents'] = [ea.agent.name for ea in EventAgent.objects.filter(event = e.event)]
			event['patients'] = [ep.patient.name for ep in EventPatient.objects.filter(event = e.event)]
			event['beneficiary'] = [eb.beneficiary.name for ea in EventBeneficiary.objects.filter(event = e.event)]
			event['location'] = [el.location.name for el in EventLocation.objects.filter(event = e.event)]
			event['time'] = [et.time.name for et in EventTime.objects.filter(event = e.event)]
			event['instrument'] = [ei.instrument.name for ea in EventInstrument.objects.filter(event = e.event)]
			res['events'].append(event)
		return res	
	
		
if __name__ == "__main__":
	e = EventInstance()
	e.insert_agent('I')
	e.insert_action('hate')
	e.insert_patient('Mango')
	q = EventQuery()
	res = q.search_action('hate')
	print res