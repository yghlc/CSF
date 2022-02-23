
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

The demo requires [PDAL](https://pdal.io/) and [laspy<2.0.0](https://github.com/laspy/laspy).
Install them first. 

```
conda activate csf
conda install pdal
pip install "laspy<2.0.0"
```

```
conda activate csf
# from tif to las, ref: https://gis.stackexchange.com/questions/264913/converting-tiff-file-to-las-file-in-qgis
# if don't set the readers.gdal.header, all z are zero
pdal translate  SETSM_GE01_20140511_for_test_CSF_v2.tif SETSM_GE01_20140511_for_test_CSF.las --readers.gdal.header="z"

# run the code
python demo_tif.py

# from las to tif
pdal pipeline pipeline.json
```

After this, we should get a DEM after applying CSF. 
The result still did not completely remove buildings, maybe still need to tweak the parameters. 


TODO: read and write tif directly without format translation.







