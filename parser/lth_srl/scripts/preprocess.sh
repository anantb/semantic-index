
MODEL=models/penn_00_18_split_dict.model
DICT=v_n_a.txt

MEM=100M
CP=jars/lthsrl.jar:jars/utilities.jar:jars/trove.jar:jars/seqlabeler.jar

java -Xmx$MEM -cp $CP se.lth.cs.nlp.depsrl.Preprocessor -allLTH $MODEL $DICT
