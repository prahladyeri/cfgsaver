"""
:title: cfgsaver
:author: Prahlad Yeri<prahladyeri@yahoo.com>
:license: MIT

This module is used to save and fetch configuration data in a standard path and format.
"""
import cfgsaver
import json, os

"""
Get Configuration Data

:param pkg_name: Name of the package
:param cfgpath, optional: Path to configuration directory
:returns: configuration data in dict, None if config file is missing
"""
def get(pkg_name , cfgpath=None):
	if cfgpath == None:
		cfgpath = os.path.expanduser("~/.config/%s" % pkg_name)
	if not os.path.isdir(cfgpath):
		os.makedirs(cfgpath)
		return None
	cfgpath = os.path.join(cfgpath,  "cfg.json")
	if not os.path.isfile(cfgpath):
		return None
	ss = open(cfgpath).read()
	return json.loads(ss)
	

"""
Save Configuration Data

:param pkg_name: Name of the package
:param cfgobject: Object to be saved (dict)
:param cfgpath, optional: Path to configuration directory
:returns: True
"""
def save(pkg_name, cfgobject, cfgpath=None):
	if cfgpath == None:
		cfgpath = os.path.expanduser("~/.config/%s" % pkg_name)
	if not os.path.isdir(cfgpath):
		os.makedirs(cfgpath)
	cfgpath = os.path.join(cfgpath,  "cfg.json")
	ss = json.dumps(cfgobject)
	open(cfgpath, 'w').write(ss)
	return True

"""
Prompt user for configuration keys and save resulting values in the configuration.

:param pkg_name: Name of the package
:param keys: List of keys
:param cfgpath, optional: Path to json file
:returns: True
"""
def get_from_cmd(pkg_name, keys):
	print("Configuration Saver version %s\n" % cfgsaver.__version__)
	obj = {}
	for key in keys:
		try: 
			obj[key] = input("Enter %s: " % key)
		except KeyboardInterrupt as ex:
			return None
	save(pkg_name, obj)
	return obj