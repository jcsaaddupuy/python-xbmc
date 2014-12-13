
[![Latest Version](https://pypip.in/version/xbmc-json/badge.svg)](https://pypi.python.org/pypi/xbmc-json/)
[![Supported Python versions](https://pypip.in/py_versions/xbmc-json/badge.svg)](https://pypi.python.org/pypi/xbmc-json/)
[![Wheel Status](https://pypip.in/wheel/xbmc-json/badge.svg)](https://pypi.python.org/pypi/xbmc-json/)
[![License](https://pypip.in/license/xbmc-json/badge.svg)](https://pypi.python.org/pypi/xbmc-json/)



python xbmc json client
=======================

Simple python module that allow xbmc control over HTTP Json API.
Virtually support all availables commands.

Install it :
```bash
pip install xbmc-json
```


Usages examples :

Client instanciation
```python
from xbmcjson import XBMC, PLAYER_VIDEO
#Login with default xbmc/xbmc credentials
xbmc = XBMC("http://YOURHOST/jsonrpc")

#Login with custom credentials
xbmc = XBMC("http://YOURHOST/jsonrpc", "login", "password")
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

# ...and so on
```

Parameters can alos be passed as python parameters:
```python
xbmc.GUI.ActivateWindow(window="home")
xbmc.GUI.ActivateWindow(window="weather")
xbmc.GUI.ShowNotification(title="Title", message = "Hello notif")
```


Library interaction :
```python
xbmc.VideoLibrary.Scan()
xbmc.VideoLibrary.Clean()
# ...and so on
```

Everything to build a script thats act as a full remote
```python
xbmc.Application.SetMute({"mute":True})
xbmc.Player.PlayPause([PLAYER_VIDEO])
xbmc.Player.Stop([PLAYER_VIDEO])
xbmc.Input.Left()
xbmc.Input.Right()
xbmc.Input.Up()
xbmc.Input.Down()
xbmc.Input.Back()
xbmc.Input.Down()
xbmc.Input.Info()
# ...and so on
```


See http://wiki.xbmc.org/index.php?title=JSON-RPC_API/v6 for availables commands.


Every XBMC namespaces are accessible from the instanciated xbmc client.

Every commands presents in the [API documentation](http://wiki.xbmc.org/index.php?title=JSON-RPC_API/v6) should be available.


You can take a look at [xbmc-client](https://github.com/jcsaaddupuy/xbmc-client) for an implementation example.


Contribute
-----------

Please make your PR on the branch develop :)
