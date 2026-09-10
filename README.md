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


The NNAdapter can also be accessed via

```
pip install -i https://test.pypi.org/simple/ olll
```
