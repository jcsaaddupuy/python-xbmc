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
    install_requires = ["requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Intended Audience :: Developers",

        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        ]
    )
