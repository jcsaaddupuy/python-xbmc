from setuptools import setup
import version

PACKAGE = 'xbmc-json'

setup(name = PACKAGE, version = version.VERSION,
    license = "WTFPL",
    description = "Python module for controlling xbmc over HTTP Json API",
    author = "Jean-Christophe Saad-Dupuy",
    author_email = "saad.dupuy@gmail.com",
    url = "https://github.com/jcsaaddupuy/python-xbmc",
    py_modules = [ "xbmcjson/xbmcjson" ],
    packages = ["xbmcjson"],
    )
