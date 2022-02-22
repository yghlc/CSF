#!/usr/bin/env python
# Filename: demo_tif.py 
"""
introduction: run a demo: applying CSF to digital surface model in GeoTiff.

authors: Huang Lingcao
email:huanglingcao@gmail.com
add time: 22 February, 2022
"""

import os,sys
deeplabforRS =  os.path.expanduser('~/codes/PycharmProjects/DeeplabforRS')
sys.path.insert(0, deeplabforRS)

import raster_io

import laspy
import CSF
import numpy as np



def main():
    # dsm_tif = 'SETSM_GE01_20140511_for_test_CSF.tif'

    dsm_las = 'SETSM_GE01_20140511_for_test_CSF.las'


    inFile = laspy.file.File(dsm_las, mode='r')  # read a las file
    points = inFile.points
    xyz = np.vstack((inFile.x, inFile.y, inFile.z)).transpose()  # extract x, y, z and put into a list

    csf = CSF.CSF()

    # prameter settings
    csf.params.bSloopSmooth = False
    csf.params.cloth_resolution = 0.5
    # more details about parameter: http://ramm.bnu.edu.cn/projects/CSF/download/

    csf.setPointCloud(xyz)
    ground = CSF.VecInt()  # a list to indicate the index of ground points after calculation
    non_ground = CSF.VecInt()  # a list to indicate the index of non-ground points after calculation
    csf.do_filtering(ground, non_ground)  # do actual filtering.

    outFile = laspy.file.File(r"ground.las",
                              mode='w', header=inFile.header)
    outFile.points = points[ground]  # extract ground points, and save it to a las file.
    outFile.close()  # do not forget this



if __name__ == '__main__':
    main()