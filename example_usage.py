#!/usr/bin/env python3

"""
.. module:: example_usage
   :synopsis: a simple example for how to use the nnAdapter
   example taken from ATLAS-SUSY-2018-04

.. author:: OLLL collaboration

"""

from hep_olll.nnAdapter import NNAdapter
onnxFile = "atlas-susy-2018-04.onnx"
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
