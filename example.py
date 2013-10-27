#!/bin_/env/python

from xbmc import XBMC, PLAYER_VIDEO

if __name__ == "__main__":
	xbmc = XBMC("http://YOURHOST/jsonrpc")
        # JSON RPC
        # Ping
        print xbmc.JSONRPC.Ping()
	
        # Gui
        xbmc.GUI.ActivateWindow({"window":"home"})
        xbmc.GUI.ActivateWindow({"window":"weather"})
        # Show a notification
        xbmc.GUI.ShowNotification({"title":"Title", "message":"Hello notif"})
        # Application
        xbmc.Application.SetMute({"mute":True})	
        xbmc.Application.SetMute({"mute":False})	
        # Video library
	xbmc.VideoLibrary.Scan()
	xbmc.VideoLibrary.Clean()
        # Query the video library
	print xbmc.VideoLibrary.GetTVShows({ "filter": {"field": "playcount", "operator": "is", "value": "0"}, "limits": { "start" : 0, "end": 75 }, "properties": ["art", "genre", "plot", "title", "originaltitle", "year", "rating", "thumbnail", "playcount", "file", "fanart"], "sort": { "order": "ascending", "method": "label" } }, id="libTvShows")
        
        #Player
	xbmc.Player.PlayPause([PLAYER_VIDEO])
	xbmc.Player.Stop([PLAYER_VIDEO])
