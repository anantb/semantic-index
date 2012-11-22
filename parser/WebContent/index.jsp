<%@ page import="java.util.Collection, java.util.List, edu.stanford.nlp.objectbank.TokenizerFactory, edu.stanford.nlp.process.CoreLabelTokenFactory, edu.stanford.nlp.process.DocumentPreprocessor, edu.stanford.nlp.process.PTBTokenizer, edu.stanford.nlp.ling.CoreLabel, edu.stanford.nlp.ling.HasWord, edu.stanford.nlp.ling.Sentence, edu.stanford.nlp.trees.*, edu.stanford.nlp.parser.lexparser.LexicalizedParser "%>

<%
  out.println("Hello World");

  LexicalizedParser lp = LexicalizedParser.loadModel("edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz");
  String[] sent = { "The", "new", "phone", "book", "and", "tour", "guide", "sold", "quickly", "." };
  List<CoreLabel> rawWords = Sentence.toCoreLabelList(sent);
  Tree parse = lp.apply(rawWords);
  parse.pennPrint();
  out.println();
  TreebankLanguagePack tlp = new PennTreebankLanguagePack();
  GrammaticalStructureFactory gsf = tlp.grammaticalStructureFactory();
  GrammaticalStructure gs = gsf.newGrammaticalStructure(parse);
  List<TypedDependency> tdl = gs.typedDependenciesCCprocessed();
  out.println(tdl);
  out.println();
  TreePrint tp = new TreePrint("penn,typedDependenciesCollapsed");
  tp.printTree(parse);
  

%>

