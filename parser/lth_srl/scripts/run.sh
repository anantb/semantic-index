SYNMODEL=models/train_at_pp_more2nd.model
LM=models/lm_080602_uknpreds.model
GM_CD=models/global_partcq_mc_cd_2o_ukp.model
GM_CL=models/part12345_cq_mc_2o_ukp.sv.model

CP=jars/lthsrl.jar:jars/utilities.jar:jars/trove.jar

MEM=2600M

NSYN=4
NSEM=4

SYNW=25
GMW=3

FORCE_VARGS=false

java -Xmx$MEM -cp $CP se.lth.cs.nlp.depsrl.Main -runFull \
 $LM \
 $GM_CD $GM_CL \
 $SYNMODEL \
 pb_frames nb_frames \
 $NSYN $NSEM \
 $SYNW $GMW \
 false false \
 $FORCE_VARGS
