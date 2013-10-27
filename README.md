python-xbmc
===========

Simple python module that allow xbmc control over HTTP Json API.
Virtually support all availables commands.

Install it :
```bash
pip install xbmc
```


Usages examples :

Client instanciation
```python
from xbmc import XBMC, PLAYER_VIDEO
xbmc = XBMC("http://YOURHOST/jsonrpc")
```
Ping XBMC
```python
print xbmc.JSONRPC.Ping()
```

UI interaction :
```python
# Navigate throught windows
xbmc.GUI.ActivateWindow({"window":"home"})
xbmc.GUI.ActivateWindow({"window":"weather"})

# Show some notifiations :
xbmc.GUI.ShowNotification({"title":"Title", "message":"Hello notif"})
```

Library interaction :
```python
xbmc.VideoLibrary.Scan()
xbmc.VideoLibrary.Clean()
```

Everything to build a script thats act as a full remote
```python
xbmc.Application.SetMute({"mute":True})
xbmc.Player.PlayPause([PLAYER_VIDEO])
xbmc.Player.Stop([PLAYER_VIDEO])
# ...and so on
```


See http://wiki.xbmc.org/index.php?title=JSON-RPC_API/v6 for availables commands.


Every XBMC namespaces are accessible from the instanciated xbmc client.

Every commands presents in the [API documentation](http://wiki.xbmc.org/index.php?title=JSON-RPC_API/v6) should be accessibles.
