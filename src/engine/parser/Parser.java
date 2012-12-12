package parser;
	
import java.util.Collection;
import java.util.List;
import java.util.ArrayList;
import java.io.StringReader;

import edu.stanford.nlp.objectbank.TokenizerFactory;
import edu.stanford.nlp.process.CoreLabelTokenFactory;
import edu.stanford.nlp.process.DocumentPreprocessor;
import edu.stanford.nlp.process.PTBTokenizer;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.HasWord;
import edu.stanford.nlp.ling.Sentence;
import edu.stanford.nlp.trees.*;
import edu.stanford.nlp.parser.lexparser.LexicalizedParser;


/**
@author: anant bhardwaj
@date: Dec 8, 2012

A class that wraps stanford parser

*/

class Parser {
	LexicalizedParser lp;
	TokenizerFactory<CoreLabel> tokenizerFactory;
	TreebankLanguagePack tlp;
	GrammaticalStructureFactory gsf;
	
	public Parser(){
		this.lp = LexicalizedParser.loadModel("edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz");
		this.tokenizerFactory =	PTBTokenizer.factory(new CoreLabelTokenFactory(), "");
		this.tlp = new PennTreebankLanguagePack();
		this.gsf = tlp.grammaticalStructureFactory();		
		
	}

	public List<String> parse(String args) {
		String[] sen = args.split("\\r?\\n");
		List<String> res = new ArrayList<String>();
		for(int i=0; i<sen.length; i++){
			if((sen[i]!=null) && (sen[i].length() >0)) {
				List<CoreLabel> tokens = this.tokenizerFactory.getTokenizer(new StringReader(sen[i])).tokenize();
				Tree parse = this.lp.apply(tokens);    
				GrammaticalStructure gs = this.gsf.newGrammaticalStructure(parse);
				List<TypedDependency> tdl = gs.typedDependenciesCCprocessed();
				res.add(tdl.toString());
			}
		}
		return res;	
	}	
}
