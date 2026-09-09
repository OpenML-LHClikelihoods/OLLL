OLLL

# Example usage (taken from ATLAS-SUSY-2019-09):

```
    regions = [ 'SRhigh_0Jb_cuts', 'SRhigh_0Jc_cuts', 'SRhigh_0Jd_cuts',
        'SRhigh_0Je_cuts', 'SRhigh_0Jf1_cuts', 'SRhigh_0Jf2_cuts',
        'SRhigh_0Jg1_cuts', 'SRhigh_0Jg2_cuts', 'SRhigh_nJa_cuts',
        'SRhigh_nJb_cuts', 'SRhigh_nJc_cuts', 'SRhigh_nJd_cuts',
        'SRhigh_nJe_cuts', 'SRhigh_nJf_cuts', 'SRhigh_nJg_cuts',
        'SRlow_0Jb_cuts', 'SRlow_0Jc_cuts', 'SRlow_0Jd_cuts',
        'SRlow_0Je_cuts', 'SRlow_0Jf1_cuts', 'SRlow_0Jf2_cuts',
        'SRlow_0Jg1_cuts', 'SRlow_0Jg2_cuts', 'SRlow_nJb_cuts',
        'SRlow_nJc_cuts', 'SRlow_nJd_cuts', 'SRlow_nJe_cuts',
        'SRlow_nJf1_cuts', 'SRlow_nJf2_cuts', 'SRlow_nJg1_cuts',
        'SRlow_nJg2_cuts', 'CR_0J_WZ_cuts', 'CR_nJ_WZ_cuts' ]
    onnxFile = "test.onnx"

    adapter = NNAdapter ( onnxFile, session_options = {} )

    yields = {}
    for region in regions: # predict for no yields
        yields[ region ] = 0.
    ret = adapter.predict ( yields )
    print ( "\n".join( f"{key:10s}: {value:.1f}" for key,value in ret.items()) )
```
