Installation
============

The `boolparser` module is pure python and requires _PyParsing. It should be possible to install from source (:ref:`from_source`) from `GitHub`_ , using (:ref:`from_PyPi`) , and from :ref:`from_conda`.

There are clearly too many install options. Use ``pip install boolparser``, if that doesn't work, try ``conda install -c chrislee boolparser``. After that I would probably give up.

.. _from_source:

=======================
Installing from source
=======================

(Assuming you can install Python packages somewhere, either in the python directory, or a virtualenv, or a conda env, etc.)

Installing from source should be as simple as

.. code-block:: bash
    
    git clone https://github.com/eelsirhc/boolparser.git
    cd boolparser
    python setup.py install

.. _from_PyPi:

=====
PyPi
=====

The latest version of `boolparser` should be on `PyPi`_, and should be installable with

.. code-block:: bash

    pip install boolparser
  
.. _from_conda:

=====
Conda
=====

The latest version of `boolparser` should be installable from Anaconda using 

.. code-block:: bash

   conda install boolparser
   
You can get the package from a few channels `eelsirhc`_, `auto`_, and `pypi <https://anaconda.org/pypi/boolparser>`__, either by adding a ``-c CHANNEL`` to the conda command or adding the channel to your configuration (`help`_).

.. _PyParsing: http://pyparsing.wikispaces.com/
.. _Github: https://github.com/eelsirhc/boolparser
.. _PyPi: https://pypi.org/project/boolparser/
.. _eelsirhc: https://anaconda.org/chrislee/boolparser
.. _auto: https://anaconda.org/auto/boolparser
.. _condapypi: https://anaconda.org/pypi/boolparser
.. _help: https://conda.io/docs/user-guide/tasks/manage-channels.html

