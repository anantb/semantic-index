import httplib, urllib


def parse(params, url='/parser/parser.jsp'):
	conn = httplib.HTTPConnection("anantb.csail.mit.edu:8080")
	headers = {"Content-type": "application/x-www-form-urlencoded",
			"Accept": "text/plain"}
	params = urllib.urlencode(params)
	conn.request("POST", url, params, headers)	
	res = conn.getresponse().read()
	return res
