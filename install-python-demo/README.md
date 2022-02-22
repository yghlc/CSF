
## Install Python API on Linux

```
# Need cmake 3.18 or 3.14,  3.10 not working.

conda env create -f tesia_csf.yml  (attached)
conda activate csf
git clone https://github.com/yghlc/CSF.git .
cd CSF/python
python setup.py build
python setup.py install
```

## run a demo
In this demo, we apply a CSF to a digital surface model (DSM), 
which is acquired on May 11, 2014 and is a subset of ArcticDEM.
It's extent is saved in AK_fairbanks_test_CSF.kml. Please be aware 
that the date of images shown in Google Earth or Google Map might 
be not in 2014.





