# Open library of learned likelihoods from LHC experiments

The release of full statistical models from LHC analyses is a major milestone in the
LHC’s legacy. They encapsulate the full information of an analysis, including the likeli-
hood given data. Thus, full releases enable collider phenomenology to be performed at full
statistical precision. However, this comes with a significant enlargement of computational
costs. For most reinterpretation processes, we are interested in the profiled likelihood,
which is slow to extract from the statistical model, particularly for analyses with mul-
tiple signal regions. To mitigate this, we present OLLL, an Open Library of Learned
Likelihoods from LHC experiments. OLLL is composed of profiled likelihood functions
modelled with Neural Networks (NNs). We show, through five examples of increasing
complexity, that such functions can be well described with simple NNs, published in the
ONNX format, and easily used by different reinterpretation tools without compromising
statistical precision.

## Example usage (taken from ATLAS-SUSY-2019-09):

```python
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
```

The NNAdapter can also be accessed via

```
pip install -i https://test.pypi.org/simple/ olll
```
