import os
import glob
modules = glob.glob('{0:s}/*.py'.format(os.path.dirname(__file__)))
__all__ = [os.path.basename(f)[:-3] for f in modules]