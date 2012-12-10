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
	print res
	temp = {}
	tags = ['root', 'nsubj', 'dobj', 'amod', 'advmod', 'conj_and']
	for tag in tags:
		try:
			v = res[tag]
			val = v[1]
			word = val[:val.find('-')]
			if(tag=='root'):
				action = e.insert_action(word)
				temp[v[1]] = action
			elif(tag =='nsubj'):
				agent = e.insert_agent(word)
				temp[v[1]] = agent
			elif(tag=='dobj'):
				patient = e.insert_patient(word)
				temp[v[1]] = patient
			elif(tag=='advmod'):
				adv = e.insert_adverb(word, temp[v[0]])
				temp[v[1]] = temp[v[0]]
			elif(tag=='amod'):
				adj  = e.insert_adjective(word, temp[v[0]])
				temp[v[1]] = temp[v[0]]
			elif(tag=='conj_and'):
				val = v[0]
				word = val[:val.find('-')]
				adj  = e.insert_adjective(word, temp[v[1]])
				temp[v[0]] = temp[v[1]]
		except KeyError:
			pass
	print temp
			
			
		



if __name__ == "__main__":
	handle_sentence('The red and green ball bounces well.')
	handle_sentence('The blue and purple ball bounces badly.', False)
	q = EventQuery()
	res = q.search_action('bounces')
	print res