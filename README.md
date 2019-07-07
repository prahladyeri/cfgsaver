![pypi](https://img.shields.io/pypi/v/cfgsaver.svg)
![python](https://img.shields.io/pypi/pyversions/cfgsaver.svg)
![license](https://img.shields.io/github/license/prahladyeri/cfgsaver.svg)
![last-commit](https://img.shields.io/github/last-commit/prahladyeri/cfgsaver.svg)
![docs](https://readthedocs.org/projects/cfgsaver/badge/?version=latest)
[![donate](https://img.shields.io/badge/-Donate-blue.svg?logo=paypal)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=JM8FUXNFUK6EU)
[![follow](https://img.shields.io/twitter/follow/prahladyeri.svg?style=social)](https://twitter.com/prahladyeri)

# cfgsaver

![project logo](https://raw.githubusercontent.com/prahladyeri/cfgsaver/master/logo.png)

Python library to save and fetch configuration data in a standard/conventional path and format.

# Installation

```bash
pip install cfgsaver
```

# Usage

Import the `cfgsaver` module to save/read configuration values in your source files:

```python
from cfgsaver import cfgsaver

def save_config():
	# saves configuration data to ~/.config/<your_package>/cfg.json
	# unless cfgpath parameter is overridden:
	config = {
	'name': 'Prahlad', 
	'language': 'Python', 
	'framework': 'Flask'
	}
	cfgsaver.save('<your_package>', config)

def get_config():
	# gets configuration data from ~/.config/<your_package>/cfg.json 
	# unless cfgpath parameter is overridden:
	config = cfgsaver.get("<your_package>") #returns None if config file doesn't exist
	
def prompt_user():
	# prompts user for config keys and saves resulting values as per save_config()
	config = {
	'name': '', 
	'language': '', 
	'framework': ''
	}
	config = cfgsaver.get_from_cmd("<your_package>", config.keys())
```

For information on shipping default configuration data packaged with your app using `setup.py`, read [detailed docs](https://cfgsaver.readthedocs.io/en/latest/).

# Documentation

Detailed docs are available at <https://cfgsaver.readthedocs.io/en/latest/>.
	
# Attribution

<div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" 		    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 		    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>