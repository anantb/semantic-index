import java.util.Collection;
import java.util.List;
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

	public static void main(String[] args) {
		LexicalizedParser lp = LexicalizedParser.loadModel("edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz");
		if (args.length < 1) {
			System.out.println("Usage : Parser <sentence>");
			System.exit(1);
		}
		String sentences = args[0];
		String[] sen = sentences.split("\\r?\\n");
		TokenizerFactory<CoreLabel> tokenizerFactory =
		PTBTokenizer.factory(new CoreLabelTokenFactory(), "");
		TreebankLanguagePack tlp = new PennTreebankLanguagePack();
		GrammaticalStructureFactory gsf = tlp.grammaticalStructureFactory();
		for(int i=0; i<sen.length; i++){
			if((sen[i]!=null) && (sen[i].length() >0)) {
				List<CoreLabel> tokens = tokenizerFactory.getTokenizer(new StringReader(sen[i])).tokenize();
				Tree parse = lp.apply(tokens);    
				GrammaticalStructure gs = gsf.newGrammaticalStructure(parse);
				List<TypedDependency> tdl = gs.typedDependenciesCCprocessed();
				System.out.println(tdl);
			}
		}

	}	
}
