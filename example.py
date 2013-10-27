#!/bin_/env/python

from xbmc import XBMC, PLAYER_VIDEO

if __name__ == "__main__":
	xbmc = XBMC("http://YOURHOST/jsonrpc")
	xbmc.Application.SetVolume(100)
	xbmc.Application.SetMute(False)
	xbmc.Gui.ActivateWindow("weather")
	xbmc.Gui.ActivateWindow("home")
	xbmc.VideoLibrary.Scan()
	xbmc.VideoLibrary.Clean()
	xbmc.Player.PlayPause([PLAYER_VIDEO])
	xbmc.Player.Stop([PLAYER_VIDEO])
	print xbmc.VideoLibrary.GetTVShows({ "filter": {"field": "playcount", "operator": "is", "value": "0"}, "limits": { "start" : 0, "end": 75 }, "properties": ["art", "genre", "plot", "title", "originaltitle", "year", "rating", "thumbnail", "playcount", "file", "fanart"], "sort": { "order": "ascending", "method": "label" } }, id="libTvShows")
        # Show a notification
        xbmc.Gui.ShowNotification({"title":"Title", "message":"Hello notif"})
