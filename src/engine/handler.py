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
def get_index(k):
	tag_order = ['root', 'nsubj', 'dobj', 'amod', 'advmod', 'conj_and']
	if k in tag_order:
		return tag_order.index(k)
	else:
		return 1000
	

def handle_sentence(tags, reset = True):
	temp = {}	
	e = EventInstance(reset)
	for tag in tags:
		k = tag[0]
		v = tag[1]		
		val = v[1]
		word = val[:val.find('-')]
		if(k=='root'):
			action = e.insert_action(word)
			temp[v[1]] = action
		elif(k =='nsubj'):
			agent = e.insert_agent(word)
			temp[v[1]] = agent
		elif(k=='dobj'):
			patient = e.insert_patient(word)
			temp[v[1]] = patient
		elif(k=='advmod'):
			adv = e.insert_adverb(word, temp[v[0]])
			temp[v[1]] = temp[v[0]]
		elif(k=='amod'):
			adj  = e.insert_adjective(word, temp[v[0]])
			temp[v[1]] = temp[v[0]]
		''''
		#this breaks many other thing, use with care
		elif(k=='conj_and'):
			val = v[0]
			word = val[:val.find('-')]
			adj  = e.insert_adjective(word, temp[v[1]])
			temp[v[0]] = temp[v[1]]
		'''

def search(sentences, action):
	if(len(sentences) == 0):
		return {}
	
	parses = [stanford_parse_local(sen) for sen in sentences]
	tags_set = [sorted(parse, key = lambda x:get_index(x[0])) for parse in parses]
	handle_sentence(tags_set[0])
	for i in xrange(1,len(tags_set)):
		handle_sentence(tags_set[i], reset = False)
	q = EventQuery()
	res = q.search_action(action)
	return res

def visualize(sentences):
	if(len(sentences) == 0):
		return {}
	parses = [stanford_parse_local(sen) for sen in sentences]
	tags_set = [sorted(parse, key = lambda x:get_index(x[0])) for parse in parses]
	handle_sentence(tags_set[0])
	for i in xrange(1,len(tags_set)):
		handle_sentence(tags_set[i], reset = False)
	q = EventQuery()
	res = q.get_tree()
	return res


if __name__ == "__main__":
	print search(['The magical instrument heavenly exemplifies the beautiful building.'], 'exemplifies')