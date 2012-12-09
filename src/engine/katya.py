from utils import *


stanford = parse({'input':'Max plays tennis well.'})
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
object = ''
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
    object = obj1[0]
    if '.' in object:
        object = object.split('.')[0]


#print subject + ' ' + event + ' ' + object+ ' ' + adjective + ' ' + adverb
 