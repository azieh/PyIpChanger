
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    name='IpChanger',
    version="1.0",
    options= {"py2exe": {"includes": ["sip"], "compressed": 1, "optimize": 0, 'dist_dir': "ExeProgram", "bundle_files": 3}},
    windows=[
        {
            'script': "main.py",
            "icon_resources": [(1, "graphic/logo.ico")],
            "dest_base": "IpManager"
        }
    ],
    zipfile=None,
)
