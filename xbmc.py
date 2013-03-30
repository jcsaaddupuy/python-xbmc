#!/bin_/env/python

import urllib, urllib2
import json

PLAYER_VIDEO=1

class XBMCTransport(object):
	def execute(self, method, args):
		pass

class XBMCJsonTransport(XBMCTransport):
	def __init__(self, url, username='xbmc', password='xbmc'):
		self.url=url
		self.username=username
		self.password=password
	def execute(self, method, *args, **kwargs):
		header = {
			'Content-Type' : 'application/json',
			'User-Agent' : 'python-xbmc'
		}
		if len(args) == 1:
			args=args[0]
		params = kwargs
		params['jsonrpc']='2.0'
		params['method']=method
		params['params']=args
		
		values=json.dumps(params)
		print values
		auth_handler = urllib2.HTTPBasicAuthHandler()
		auth_handler.add_password(realm=None,
                          uri=self.url,
                          user=self.username,
                          passwd=self.password)
		opener = urllib2.build_opener(auth_handler)
		# ...and install it globally so it can be used with urlopen.
		urllib2.install_opener(opener)
		#return None
		data = values
		req = urllib2.Request(self.url, data, header)
		response = urllib2.urlopen(req)
		the_page = response.read()
		return the_page

class XBMC(object):
	def __init__(self, url, username='xbmc', password='xbmc'):
		self.transport = XBMCJsonTransport(url, username, password)
		self.VideoLibrary = VideoLibrary(self.transport)	
		self.Application = Application(self.transport)	
		self.Gui = Gui(self.transport)	
		self.Player = Player(self.transport)	
	def execute(self, *args, **kwargs):
		self.transport.execute(*args, **kwargs)

class XbmcNamespace(object):
	def __init__(self, xbmc):
		self.xbmc = xbmc
	def __getattr__(self, name):
		klass= self.__class__.__name__
		method=name
		xbmcmethod = "%s.%s"%(klass, method)
		def hook(*args, **kwargs):
			return self.xbmc.execute(xbmcmethod, *args, **kwargs)
		return hook
	
class VideoLibrary(XbmcNamespace):
	pass
class Application(XbmcNamespace):
	pass
class Gui(XbmcNamespace):
	pass
class Player(XbmcNamespace):
	pass

if __name__ == "__main__":
	xbmc = XBMC("http://ida/jsonrpc")
	#xbmc.Application.SetVolume(100)
#	xbmc.Application.SetMute(False)
	#xbmc.Gui.ActivateWindow("weather")
	#xbmc.Gui.ActivateWindow("home")
	#xbmc.VideoLibrary.Scan()
	#xbmc.VideoLibrary.Clean()
	#xbmc.Player.PlayPause([PLAYER_VIDEO])
	#xbmc.Player.Stop(PLAYER_VIDEO)
	#xbmc.VideoLibrary.GetTVShows({ "filter": {"field": "playcount", "operator": "is", "value": "0"}}, id="libTvShows")
	#print xbmc.VideoLibrary.GetTVShows({ "filter": {"field": "playcount", "operator": "is", "value": "0"}, "limits": { "start" : 0, "end": 75 }, "properties": ["art", "genre", "plot", "title", "originaltitle", "year", "rating", "thumbnail", "playcount", "file", "fanart"], "sort": { "order": "ascending", "method": "label" } }, id="libTvShows")
