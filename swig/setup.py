"""
setup.py file for SWIG teste
"""

from distutils.core import setup, Extension
import os

mod_name = 'pyDEM'
files = ["../core/"+each for each in os.listdir("../core") if each.endswith('.cpp') or each.endswith('.cxx')] + [mod_name+"_wrap.cxx"]

ext_mod = Extension('_'+mod_name, sources = files)

setup (name = mod_name,
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig teste from docs""",
       ext_modules = [ext_mod],
       py_modules = [mod_name],
       )