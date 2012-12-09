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

class Parser {

	public static void main(String[] args) {
		LexicalizedParser lp = LexicalizedParser.loadModel("edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz");
		if (args.length < 1) {
			System.out.println("Usage : Parser <sentence>");
			System.exit(1);
		}
		String sen = args[0];
		TokenizerFactory<CoreLabel> tokenizerFactory =
		PTBTokenizer.factory(new CoreLabelTokenFactory(), "");
		List<CoreLabel> tokens = tokenizerFactory.getTokenizer(new StringReader(sen)).tokenize();
		Tree parse = lp.apply(tokens);    
		TreebankLanguagePack tlp = new PennTreebankLanguagePack();
		GrammaticalStructureFactory gsf = tlp.grammaticalStructureFactory();
		GrammaticalStructure gs = gsf.newGrammaticalStructure(parse);
		List<TypedDependency> tdl = gs.typedDependenciesCCprocessed();
		System.out.println(tdl);

	}	
}
