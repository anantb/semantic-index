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
	temp = {}
	for k, v in res.iteritems():
		val = v[1]
		word = val[:val.find('-')]
		if(k == 'root'):
			action = e.insert_action(word)
			temp[v[1]] = action
		elif(k=='nsubj'):
			agent = e.insert_agent(word)
			temp[v[1]] = agent
		elif(k=='dobj'):
			patient = e.insert_patient(word)
			temp[v[1]] = patient
		elif(k=='advmod'):
			e.insert_adverb(word, temp[v[0]])
		elif(k=='amod'):
			e.insert_adjective(word, temp[v[0]])
		
		
			
			
		



if __name__ == "__main__":
	handle_sentence('The red ball bounces well.')
	q = EventQuery()
	res = q.search_action('bounces')
	print res