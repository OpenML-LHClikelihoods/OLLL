#!/usr/bin/env python3

from nnAdapter import NNAdapter
regions = [ 'SR1cut_cuts-0', 'SR2cut_cuts-0' ]
onnxFile = "test.onnx"

adapter = NNAdapter ( onnxFile, session_options = {} )

yields = {}
yields = adapter.onnxMeta["bkg_yields"]
for srname, bkg_yield in yields.items():
    ## add a signal here
    yields[srname] += 0.
ret = adapter.predict ( yields )

for srname,smyield in yields.items():
    print ( srname, smyield )

print ( "\n".join( f"{key:10s}: {value:.1f}" for key,value in ret.items()) )
