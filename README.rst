====================
comp20230TermProject
====================


.. image:: https://img.shields.io/pypi/v/comp20230termproject.svg
        :target: https://pypi.python.org/pypi/comp20230termproject

.. image:: https://img.shields.io/travis/xinyuewang1/comp20230termproject.svg
        :target: https://travis-ci.org/xinyuewang1/comp20230termproject

.. image:: https://readthedocs.org/projects/comp20230termproject/badge/?version=latest
        :target: https://comp20230termproject.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Term project, calculate the cheapest route among certain cities with certain aircraft.


* Free software: GNU General Public License v3
* Documentation: https://comp20230termproject.readthedocs.io.


----------------------------------------------------------
*****Features*****Read here to see how to use this package
----------------------------------------------------------
Two way to use through terminal:

* Go to comp20230termproject directory, start the terminal here, run
'python cli.py'. 
	Options:
	  -i TEXT    Input file for route calculation.
	  --ac TEXT  Mandatory Columns: code, units, range
	  --aa TEXT  Mandatory Columns: AirportName, Country, Latitude, Longitude
	  --ci TEXT  Mandatory Columns: CurrencyCode, toEUR
	  --cc TEXT  Mandatory Columns: name, currency_alphabetic_code
	  -o TEXT    Output to a named file.
	  --help     Show this message and exit.

	It will prompt for input/output file if you don't type it in directly.

* Install this package from github repository:
	
	pip install git+https://github.com/xinyuewang1/cheapestFlyingPlan.git
	Then run 'xinyuewang' is the same as 'python cli.py' above.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
