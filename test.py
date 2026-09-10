#!/usr/bin/env python3

from nnAdapter import NNAdapter
regions = [ 'SR1cut_cuts', 'SR2cut_cuts' ]
onnxFile = "test.onnx"                                                          
                                                                                
adapter = NNAdapter ( onnxFile, session_options = {} )                          
                                                                                
yields = {}                                                                     
for region in regions: # predict for no yields                                  
    yields[ region ] = 0.                                                       
ret = adapter.predict ( yields )                                                
print ( "\n".join( f"{key:10s}: {value:.1f}" for key,value in ret.items()) ) 
