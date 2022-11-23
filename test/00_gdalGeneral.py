import sys
from osgeo import gdal
import warnings
warnings.filterwarnings("ignore")

version_num = int(gdal.VersionInfo('VERSION_NUM'))
print(version_num)
if version_num < 1100000:
    sys.exit('ERROR: Python bindings of GDAL 1.10 or later required')