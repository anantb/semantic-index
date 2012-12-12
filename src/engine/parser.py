import subprocess, os, re, httplib, urllib, re
path = os.path.abspath(os.path.dirname(__file__))


'''
@author: anant bhardwaj
@date: Dec 8, 2012

a wrapper over third-party parsers
'''

def stanford_parse_local(sen):
	cmd = ["java -classpath %s/stanford-parser.jar:%s/stanford-parser-2.0.4-models.jar:%s: Parser '%s'" %(path,path,path, sen)]
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell = True)
	out, err = p.communicate()
	out = str(out.strip())
	out = re.split(r'\n', out)
	res = []
	for x in out:
		z = re.findall(r'(\w+?\(.+?\))', x)
		sen = []
		for i in xrange(0, len(z)):
			p = z[i][:z[i].find('(')]
			q = z[i][z[i].find('(')+1: z[i].find(',')]
			r = z[i][z[i].find(',')+1:-1].strip()
			sen.append([p, [q,r]])
		res.append(sen)
	return res


def propbank_parse_web(sen, url='/parse'):
	conn = httplib.HTTPConnection('barbar.cs.lth.se:8081')
	headers = {"Content-type": "application/x-www-form-urlencoded",
			"Accept": "text/plain"}
	params = {'sentence':sen, 'returnType':'text', 'doRenderDependencyGraph':'on'}
	params = urllib.urlencode(params)
	conn.request("POST", url, params, headers)	
	out = conn.getresponse().read()
	res = {}
	lines = re.split('\n', out)
	for line in lines:
		c = re.split('\t', line)
		res[c[0]] = c[11]
	return res
	


# do not use this (use local version instead)
def stanford_parse_web(sen, url='/parser/parser.jsp'):
	conn = httplib.HTTPConnection("anantb.csail.mit.edu:8080")
	headers = {"Content-type": "application/x-www-form-urlencoded",
			"Accept": "text/plain"}
	params = {'input':sen}
	params = urllib.urlencode(params)
	conn.request("POST", url, params, headers)	
	res = conn.getresponse().read().strip()
	return res	
	
x= """
I hate NLP.
I love NLP.
"""
if __name__ == "__main__":
	print stanford_parse_local(x)
	#print propbank_parse_web('She won because she played well.')
	#print x
	#print propbank_parse_web('I hate NLP')
	#print stanford_parse_web('I hate NLP')
