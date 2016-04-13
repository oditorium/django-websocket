# django-websocket
_An Example Websocket Installation_

## Installation

### Requirements

- Python 3.5+
- websockets (`pip3 install websockets`, [doc][wsdoc], [git][wsgit], [pypi][wspypi])

[wsdoc]:https://websockets.readthedocs.org/en/stable/
[wsgit]:https://github.com/aaugustin/websockets
[wspypi]:https://pypi.python.org/pypi/websockets

#### Installing Python 3.5 on Ubuntu 14.04

This installs Python 3.5.1 into `/opt/python3.5`: (see [here](http://askubuntu.com/questions/680824/how-do-i-update-python-from-3-4-3-to-3-5))

	wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz
	tar xfvJ Python-3.5.1.tar.xz
	cd Python-3.5.1
	./configure --prefix=/opt/python3.5
	make
### On Heroku
After installing the Heroku [Toolbelt](https://toolbelt.heroku.com/) run the following commands:

	git clone https://github.com/oditorium/django-websocket.git
	cd django-websocket
	heroku create
	heroku config:set HEROKU=1
	git push heroku +master

## Contributions

Contributions welcome. Send us a pull request!


## Change Log


The idea is to use [semantic versioning](http://semver.org/), even though initially we might make some minor
API changes without bumping the major version number. Be warned!

