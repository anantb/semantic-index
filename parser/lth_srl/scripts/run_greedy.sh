SYNMODEL=models/train_at_pp_more2nd.model
SEMMODEL=models/lm_080602_uknpreds.model

CP=jars/lthsrl.jar:jars/utilities.jar:jars/trove.jar

MEM=1500M

java -Xmx$MEM -cp $CP se.lth.cs.nlp.depsrl.Main -runLMSynSem $SEMMODEL pb_frames nb_frames $SYNMODEL
