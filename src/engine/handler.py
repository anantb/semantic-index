from parser import *
from db import *
from server.models import *

'''
@author: anant bhardwaj
@date: Dec 8, 2012

Main Handler

'''

def get_index(k):
	tag_order = ['root', 'nsubj', 'nsubjpass', 'dobj', 'agent', 'pobj', 'det', 'prep_in', 
	'prep_on', 'prep_at', 'prep_along', 'prep_during', 'tmod', 'prep_of', 'poss', 'amod', 'advmod']
	if k in tag_order:
		return tag_order.index(k)
	else:
		return 1000

def get_prep_pos(sen, index, prep):
	tokens = re.split(r' ', sen)
	tokens = filter(lambda x: x!=' ', tokens)
	for i in xrange(index-1, -1, -1):
		if(tokens[i] == prep):
			return i
	return -1

def handle_sentence(tags, pb_tags = None, sen = None, session = None):
	temp = {}	
	e = EventInstance(session)
	for tag in tags:
		k = tag[0]
		v = tag[1]		
		val = v[1]
		word = val[:val.find('-')]
		if(k in ['root']):
			action = e.insert_action(word)
			temp[v[1]] = action
		elif(k in ['nsubj', 'agent', 'pobj']):
			agent = e.insert_agent(word)
			temp[v[1]] = agent
		elif(k in ['dobj', 'nsubjpass']):
			patient = e.insert_patient(word)
			temp[v[1]] = patient
		elif(k in ['advmod']):
			try:
				adv = e.insert_adverb(word, temp[v[0]])
				temp[v[1]] = temp[v[0]]
			except KeyError:
				pass			
		elif(k in ['amod']):
			try:
				adj  = e.insert_adjective(word, temp[v[0]])
				temp[v[1]] = temp[v[0]]
			except KeyError:
				pass
		elif(k in ['det']):
			try:
				adj  = e.insert_determiner(word, temp[v[0]])
				temp[v[1]] = temp[v[0]]
			except KeyError:
				pass
		elif(k in ['prep_in', 'prep_on', 'prep_at', 'prep_along', 'prep_during', 'tmod', 'prep_of', 'poss']):
			idx = int(val[val.index('-')+1:])
			prep = k[k.index('_')+1:]
			pos = get_prep_pos(sen, idx-1, prep)
			pb_tag = pb_tags[str(pos+1)]
			if(pb_tag == 'TMP'):
				time = e.insert_time(word, action)
				temp[v[1]] = time
				continue
			if(pb_tag == 'LOC'):
				location = e.insert_location(word, action)
				temp[v[1]] = location
				continue
			if(pb_tag == 'DIR'):
				location = e.insert_location(word, action)
				temp[v[1]] = location
				continue
			patient = e.insert_patient(word)
			temp[v[1]] = patient
	return e.get_session()

def search(sentences, action):
	if(len(sentences) == 0):
		return {}
	parses = stanford_parse_local('\n'.join([sen for sen in sentences]))
	tags_set = [sorted(parse, key = lambda x:get_index(x[0])) for parse in parses]
	pb_tags_set = [propbank_parse_web(sen) for sen in sentences]
	session = handle_sentence(tags_set[0],sen = sentences[0], pb_tags = pb_tags_set[0])
	for i in xrange(1,len(tags_set)):
		handle_sentence(tags_set[i], pb_tags = pb_tags_set[i], sen = sentences[i], session = session)
	q = EventQuery(session)
	res = q.search_action(action)
	return res


def visualize(sentences):
	if(len(sentences) == 0):
		return {}
	parses = stanford_parse_local('\n'.join([sen for sen in sentences]))
	tags_set = [sorted(parse, key = lambda x:get_index(x[0])) for parse in parses]
	pb_tags_set = [propbank_parse_web(sen) for sen in sentences]
	session = handle_sentence(tags_set[0],sen = sentences[0], pb_tags = pb_tags_set[0])
	for i in xrange(1,len(tags_set)):
		handle_sentence(tags_set[i], pb_tags = pb_tags_set[i], sen = sentences[i], session = session)
	q = EventQuery(session)
	res = q.get_tree()
	return res


if __name__ == "__main__":
	print search(['The magical instrument heavenly exemplifies the beautiful building.'], 'exemplifies')