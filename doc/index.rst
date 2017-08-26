.. boolparser documentation master file, created by
   sphinx-quickstart on Sat Aug 26 04:57:12 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Boolparser
======================================



This package defines a simple boolean parser using PyParsing that allows user defined variables and floating point numbers to be used in a nested boolean comparison. For example, if the variables `a`,`b`, and `c` are defined then the following string can be parsed

     (a==1 & b<2) | c>4

The resolution of `a`, `b`, and `c` is left up to the user by inheriting from the class `EvaluateVariable` class and overriding the `eval` function. This allows the variables to be references to (say) data stored in a file.


.. toctree::
   :maxdepth: 2

   installation
   example
   license
   
   
