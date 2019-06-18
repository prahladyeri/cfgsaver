![pypi](https://img.shields.io/pypi/v/cfgsaver.svg)
![python](https://img.shields.io/pypi/pyversions/cfgsaver.svg)
![implementation](https://img.shields.io/pypi/implementation/cfgsaver.svg)
<!-- https://img.shields.io/travis/prahladyeri/cfgsaver/master.svg -->
<!-- ![docs](https://readthedocs.org/projects/cfgsaver/badge/?version=latest) -->
![license](https://img.shields.io/github/license/prahladyeri/cfgsaver.svg)
![last-commit](https://img.shields.io/github/last-commit/prahladyeri/cfgsaver.svg)
<!--![commit-activity](https://img.shields.io/github/commit-activity/w/prahladyeri/cfgsaver.svg)-->
[![donate](https://img.shields.io/badge/-Donate-blue.svg?logo=paypal)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=JM8FUXNFUK6EU)
[![follow](https://img.shields.io/twitter/follow/prahladyeri.svg?style=social)](https://twitter.com/prahladyeri)
# cfgsaver

![project logo](https://raw.githubusercontent.com/prahladyeri/cfgsaver/master/logo.png)

Python library to save and fetch configuration data in a standard/conventional path and format.

# Installation

	pip install cfgsaver
	
# Usage

Import the `cfgsaver` module to save/read configuration values in your source files:

	from cfgsaver import cfgsaver

	def save_config():
		# saves configuration data to ~/.config/<your_package>/cfg.json
		# unless cfgpath parameter is overridden:
		config = {'name': 'Prahlad', 'language': 'Python', 'framework': 'Flask'}
		cfgsaver.save('<your_package>', config)
	
	def get_config():
		# gets configuration data from ~/.config/<your_package>/cfg.json 
		# unless cfgpath parameter is overridden:
		config = cfgsaver.get("<your_package>") #returns empty dict if config file doesn't exist
		


While Packaging, ensure to include the full path to your ~/.config/<your_package> in `MANIFEST.in` as follows (depending on your OS):

	include /home/<username>/.config/<your_package>/cfg.json #linux
	
	include /c/users/<username>/.config/<your_package>/cfg.json #Windows
		
Override the PostInstall class in your setup.py like this in order to save your config file to the user's machine after installation:

	from setuptools import setup, find_packages
	from setuptools.command.install import install
	import shutil
	
	class PostInstallCommand(install):
		"""Post-installation for installation mode."""
		def run(self):
			install.run(self)
			fpath = os.path.join(self.install_lib, your_package)
			fpath = os.path.join(fpath, "cfg.json")
			tpath = os.path.join(os.path.expanduser("~"), ".config/<your_package>/cfg.json")
			if not os.path.isdir(tpath):
				os.makedirs(tpath)
			shutil.move(fpath, tpath)
			
	## setup function:
	
	setup(
	name = "your_package",
	packages=find_packages(),
	..
	..
	..
	cmdclass={
		'install': PostInstallCommand,
	},
	)

	
# Notes

[Read this article](https://prahladyeri.com/blog/2019/06/creating-a-standard-config-saver-python.html) to fully understand the synopsis for this tool.
