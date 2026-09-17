#!/usr/bin/env python3

"""
.. module:: example_with_crs
   :synopsis: a slighty more involved example for how to use
   the nnAdapter, including control regions
   example taken from ATLAS-SUSY-2019-09

.. author:: OLLL collaboration

"""

from hep_olll.nnAdapter import NNAdapter
onnxFile = "atlas-susy-2019-09.onnx"

adapter = NNAdapter ( onnxFile, session_options = {} )

bkg_yields = adapter.onnxMeta [ "bkg_yields" ]
import sys, IPython; IPython.embed( colors = "neutral" ); sys.exit()

ret = adapter.predict ( bkg_yields, yields_are_signal_yields = False,
       obs_as_bg = [] )
print ( "predicting for total yields (prefit):" )
print ( "\n".join( f"{key:10s}: {value:.3f}" for key,value in ret.items()) )

sig_yields = { k: 0. for k in bkg_yields }
ret = adapter.predict ( sig_yields, yields_are_signal_yields = True,
                        obs_as_bg = None )

print ( )
print ( f"predicting for signal yields (postfit):" )
print ( "\n".join( f"{key:10s}: {value:.3f}" for key,value in ret.items()) )
print ( )

sig_yields = { k: 0. for k in bkg_yields }
# the following two do the same thing
obs_as_bg = [ "WZ_CR_0jets_cuts-0", "WZ_CR_HighHT_cuts-0", "WZ_CR_LowHT_cuts-0" ]
obs_as_bg = "default"
ret = adapter.predict ( sig_yields, yields_are_signal_yields = True,
                        obs_as_bg = None )

print ( )
print ( f"predicting for signal yields (postfit):" )
print ( "\n".join( f"{key:10s}: {value:.3f}" for key,value in ret.items()) )
print ( )
