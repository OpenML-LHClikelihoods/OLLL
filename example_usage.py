#!/usr/bin/env python3

from nnAdapter import NNAdapter
regions = [ 'SR1cut_cuts-0', 'SR2cut_cuts-0' ]
onnxFile = "test.onnx"

adapter = NNAdapter ( onnxFile, session_options = {} )

bkg_yields = adapter.onnxMeta["bkg_yields"]
ret = adapter.predict ( bkg_yields, yields_are_signal_yields = False )
print ( "predicting for total yields:" )
print ( "\n".join( f"{key:10s}: {value:.1f}" for key,value in ret.items()) )

sig_yields = { k: 0. for k in bkg_yields }
ret = adapter.predict ( sig_yields, yields_are_signal_yields = True )

print ( )
print ( f"predicting for signal yields:" )
print ( "\n".join( f"{key:10s}: {value:.1f}" for key,value in ret.items()) )
print ( )
