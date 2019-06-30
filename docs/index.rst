.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
Introduction
============================

`cfgsaver <https://github.com/prahladyeri/cfgsaver>`_ is a python library to save and fetch configuration data in a standard or conventional path and format. By default, it saves the configuration data in `JSON` format to the ``~/.config/<pkg_name>/cfg.json`` where `~` represents the user's home directory.

Installation
===========================

.. code-block:: bash

	pip install cfgsaver

Usage
===========================

Import the `cfgsaver` module to save/read configuration values in your source files:

.. code-block:: python

	from cfgsaver import cfgsaver

	def save_config():
		# saves configuration data to ~/.config/<your_package>/cfg.json
		# unless cfgpath parameter is overridden:
		config = {'name': 'Prahlad', 
		'language': 'Python', 
		'framework': 'Flask'
		}
		cfgsaver.save('<your_package>', config)

	def get_config():
		# gets configuration data from ~/.config/<your_package>/cfg.json 
		# unless cfgpath parameter is overridden:
		config = cfgsaver.get("<your_package>") #returns None if config file doesn't exist

This will save the configuration data to `~/.config/<your_package>/cfg.json` on both linux and windows.

In case you want to ship some default configuration data packaged with your app, then read the below instructions carefully:

Ensure to include the path to your cfg.json in `MANIFEST.in` as follows (you'll have to copy this file from ~/.config/<your_package> to your source directory for packaging purpose)::

	include <your_package>/cfg.json
		
Override the PostInstall class in your setup.py like this in order to save your config file to the user's machine after installation:

.. code-block:: python

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

	s = setup(
		name = "your_package",
		packages=find_packages(),
		..
		..
		..
		cmdclass={
			'install': PostInstallCommand,
		},
	)
	
Attribution
=============

.. raw:: html

	<div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" 		    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 		    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>


Indices and tables
===========================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
