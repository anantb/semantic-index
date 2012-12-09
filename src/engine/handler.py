from parser import *
from db import *

"""
	e = EventInstance()
	agent1 = e.insert_agent('John')
	agent2 = e.insert_agent('Josh')
	action = e.insert_action('cut')
	patient = e.insert_patient('the mango')
	instrument = e.insert_instrument('with a knife', action)
	time = e.insert_time('on 5 pm', action)
	location = e.insert_location('at Stata Center', action)
	adj1 = e.insert_adjective('Hungry', agent1)
	adj2 = e.insert_adjective('angry', agent2)
	adv = e.insert_adverb('properly', action)
"""
def handle_sentence(sen, reset = True):
	e = EventInstance(reset)
	res = stanford_parse_local(sen)
	temp = {'action':None, 'agent':None, 'patient': None}
	for k, v in res.iteritems():
		val = v[1]
		val = val[:val.find('-')]
		if(k == 'root'):
			temp['action'] = e.insert_action(val)
		elif(k=='nsubj'):
			temp['agent'] = e.insert_agent(val)
		elif(k=='dobj'):
			temp['patient'] = e.insert_patient(val)
		
			
			
		



if __name__ == "__main__":
	handle_sentence('Blue Max plays tennis well.')
	q = EventQuery()
	res = q.search_action('plays')
	print res