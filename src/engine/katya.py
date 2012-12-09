from parser import *
from db import *


stanford = stanford_parse_local('Blue Max plays tennis well.')
sstanford = stanford.split('),')
print sstanford
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
    adj1 = adj[1].split('-')
    adjective = adj1[0]
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
    adv1 = adv[1].split('-')
    adverb = adv1[0]
    if '.' in adverb:
        adverb = adverb.split('.')[0]
if obj != '':
    obj = obj.split(', ')
    obj1 = obj[1].split('-')
    objec = obj1[0]
    if '.' in objec:
        objec = objec.split('.')[0]
		
e = EventInstance()
agent1 = e.insert_agent(subject)
action = e.insert_action(event)
patient = e.insert_patient(objec)
#instrument = e.insert_instrument('with a knife', action)
#time = e.insert_time('on 5 pm', action)
#location = e.insert_location('at Stata Center', action)
adj1 = e.insert_adjective(adjective, agent1)
#adj2 = e.insert_adjective('angry', agent2)
adve = e.insert_adverb(adverb, action)

q = EventQuery()
res = q.search_action('plays')
print res
		

print subject + ' ' + event + ' ' + objec + ' ' + adjective + ' ' + adverb
 