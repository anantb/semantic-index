import subprocess, os, re, httplib, urllib
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
	return str(out.strip())
	
	

def stanford_parse_web(params, url='/parser/parser.jsp'):
	conn = httplib.HTTPConnection("anantb.csail.mit.edu:8080")
	headers = {"Content-type": "application/x-www-form-urlencoded",
			"Accept": "text/plain"}
	params = urllib.urlencode(params)
	conn.request("POST", url, params, headers)	
	res = conn.getresponse().read()
	return res	
	
if __name__ == "__main__":
	print stanford_parse_local('I hate NLP')