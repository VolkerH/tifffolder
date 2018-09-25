import os
import numpy as np
import tifffile
import tifffolder

folder = 'C:/Users/Volker/Data/forTalley/'

# u: Tile number in stage X direction
# v: Tile number in stage Y direction
# d: illumination direction (the Ultramicroscopy mileading labels these as channels)
# s: z-slice (if specified as 'z', it is dropped in the shape)


#
# The following pattern finds all the files and reports the right shape. 
# 
pattern = {'u':'{d} x', 'w':'x {d}', 'd': 'C{d2}', 's': ' Z{d}'}
f = tifffolder.TiffFolder(folder, pattern, axes ='uwds' )

# Output:
# shape (2, 3, 2, 5, 2560, 2160)

# The patterns below are identical 
# to the pattern above except for the 
# naming of dictionary keys.
# However they produce pathological results when trying
# to instantiate a TiffFolder object.
# Patterns with such dictionary keys are given as
# examples in https://github.com/tlambert03/tifffolder/blob/master/README.md
# under "Specifying filename patterns:". They probably work fine with _parse_filenames
# but can't be be used with TiffFolder()

# Issue:
# pattern with multi-character dictionary keys lead to files
# being exluded while parsing. The tiffolder Readme.md  provides
# examples for such patterns with multicharacter keys. 
#
# Sample:code
#  
#pattern = {'u':'{d} x', 'w':'x {d}', 'illum': 'C{d2}', 's': ' Z{d}'}
#f = tifffolder.TiffFolder(folder, pattern)
#
# Output:
# WARNING: 55 files were excluded during parsing. Use TiffFolder.list_excluded() to show excluded files. Provided patterns may not match files.
# nr of files excluded 55
# shape (5, 2560, 2160)

# Issue
# Passing a dictionary key of 'z' for the z slice leads
# to the z-dimension being dropped from the shape:
# Similar errors also occur with dictionary keys named 'x' and 'y'
# 
# Sample Code:
#pattern = {'u':'{d} x', 'w':'x {d}', 'd': 'C{d2}', 'z': ' Z{d}'}
#f = tifffolder.TiffFolder(folder, pattern, axes ='uwdz' )
# 
# Output:
# shape (2, 3, 2, 2560, 2160)

print("nr of files excluded" , len(f.list_excluded()))
#print("files", f.files)
print("shape", f.shape)

# When trying to access the data a shape error is thrown.
print("pixel", f[0,0,0,0,0,0])