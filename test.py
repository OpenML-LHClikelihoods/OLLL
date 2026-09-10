#!/usr/bin/env python3

from nnAdapter import NNAdapter
regions = [ 'SR1cut_cuts-0', 'SR2cut_cuts-0' ]
onnxFile = "test.onnx"                                                          
                                                                                
adapter = NNAdapter ( onnxFile, session_options = {} )                          
                                                                                
yields = {}
bkg_yields = adapter.onnxMeta["bkg_yields"]
for region in regions: # predict for no yields                                  
    yields[ region ] = bkg_yields[region]
ret = adapter.predict ( yields )                                                

for srname,smyield in bkg_yields.items():
    print ( srname, smyield )
   
print ( "\n".join( f"{key:10s}: {value:.1f}" for key,value in ret.items()) ) 
