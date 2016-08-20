""" XBMC/Kodi jsonclient library module"""
import json
import requests

# XBMC constant
PLAYER_VIDEO = 1

# Dynamic namespace class injection
__XBMC_NAMESPACES__ = (
    "Addons",

    "Application",
    "AudioLibrary",

    "Favourites",
    "Files",
    "GUI",
    "Input",
    "JSONRPC",

    "Playlist",
    "Player",
    "PVR",

    "Settings",
    "System",

    "VideoLibrary",
    "xbmc"
)


class XBMCTransport(object):
    """Base class for XBMC transport"""

    def execute(self, method, args):
        pass  # pragma: no cover


class XBMCJsonTransport(XBMCTransport):
    """HTTP Json transport"""

    def __init__(self, url, username='xbmc', password='xbmc'):
        self.url = url
        self.username = username
        self.password = password
        self.id = 0

    def execute(self, method, *args, **kwargs):
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'python-xbmc'
        }
        # Params are given as a dictionnary
        if len(args) == 1:
            args = args[0]
            params = kwargs
            # Use kwargs for param=value style
        else:
            args = kwargs
        params = {}
        params['jsonrpc'] = '2.0'
        params['id'] = self.id
        self.id += 1
        params['method'] = method
        params['params'] = args

        values = json.dumps(params)

        resp = requests.post(self.url,
                             values.encode('utf-8'),
                             headers=headers,
                             auth=(self.username, self.password))
        resp.raise_for_status()
        return resp.json()


class XBMC(object):
    """XBMC client"""

    def __init__(self, url, username='xbmc', password='xbmc'):
        self.transport = XBMCJsonTransport(url, username, password)
        # Dynamic namespace class instanciation
        # we obtain class by looking up in globals
        _globals = globals()
        for cl in __XBMC_NAMESPACES__:
            setattr(self, cl, _globals[cl](self.transport))

    def execute(self, *args, **kwargs):
        self.transport.execute(*args, **kwargs)


class XBMCNamespace(object):
    """Base class for XBMC namespace."""

    def __init__(self, xbmc):
        self.xbmc = xbmc

    def __getattr__(self, name):
        klass = self.__class__.__name__
        method = name
        xbmcmethod = "%s.%s" % (klass, method)

        def hook(*args, **kwargs):
            return self.xbmc.execute(xbmcmethod, *args, **kwargs)

        return hook


# inject new type in module locals
_locals = locals()
for cl in __XBMC_NAMESPACES__:
    # define a new type extending XBMCNamespace
    # equivalent to
    #
    # class Y(XBMCNamespace):
    #    pass
    _locals[cl] = type(cl, (XBMCNamespace,), {})
