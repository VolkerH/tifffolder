import os
import numpy as np
import tifffile
import tifffolder
import pathlib

pattern = {'u':'{d} x', 'w':'x {d}', 'd': 'C{d2}', 's': ' Z{d}'}
f = tifffolder.TiffFolder('C:/Users/Volker/Data/180903_UM_Test/tmp', pattern, axes ='uwds' )
print("excluded" , f.list_excluded())
print("files", f.files)
print("shape", f.shape)
print("pixel", f[0,0,0,0,0,0])