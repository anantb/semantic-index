import subprocess, os, re, pickle
path = os.path.abspath(os.path.dirname(__file__))

def parse(sen):
	cmd = ["java -classpath %s/stanford-parser.jar:%s/stanford-parser-2.0.4-models.jar:%s: Parser '%s'" %(path,path,path, sen)]
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell = True)
	out, err = p.communicate()
	return str(out.strip())
	
	
	
	
if __name__ == "__main__":
	print parse('I hate NLP')