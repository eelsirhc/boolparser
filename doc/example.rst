Example
=========


==================
A trivial example
==================

The simplest example is to use the code to compare dictionary elements with numbers.
First define the dictionary (this would be done dynamically in reality)

.. code-block:: python
  
    from boolparser import BoolParser, EvaluateVariable
    mydict = dict(a=4, b=5, c=6, d=7, e=8, f=9, g=10, h=False)
    
and overload the ``EvaluateVariable`` class to interpret strings as dictionary items

.. code-block:: python

    class ev_dict(EvaluateVariable):
        def eval(self):
            # self.value is available
            return mydict.get(self.value,False)

and initialize the parser

.. code-block:: python

    bp = BoolParser(ev_dict)
    
Now you can call the `parse` member to parse strings:

.. code-block:: python
    
    print ( bp.parse("a>0") )
    print ( bp.parse("(a>0)&(b<4)"))
    
    
Clearly, this example is convoluted. If your dictionary is statically defined probably don't need to parse arbitrary conditionals. For this example `boolparser` is just a bad python interpreter with few features. 

==========================
A more useful example (?)
==========================

boolparser was designed to allow command line filtering of NetCDF data (e.g. "Longitude>90&Latitude>45..."). The example below uses it to filter the `Iris <https://en.wikipedia.org/wiki/Iris_flower_data_set>`_ dataset using the Python Pandas library.

.. code-block:: python

    """Setup code"""
    import statsmodels
    from boolparser import BoolParser, EvaluateVariable

    iris = statsmodels.datasets.get_rdataset("iris").data

    # convert the columns names into a useable format with current boolparser
    oldcols = iris.columns
    newcols = [c.replace(".", "_") for c in oldcols]
    iris = iris.rename(columns=dict(zip(oldcols, newcols)))

.. code-block:: python

    # Parser version
    class iris_ev(EvaluateVariable):
        def eval(self):
            return iris[self.value]

    bp = BoolParser(iris_ev)

    # Select rows where sepal length > 6 and sepal width < 3
    parsed = iris[bp.parse("(Sepal_Length>6)&(Sepal_Width<3)")]
    print(parsed.describe())

This is equivalent to the following Python code, but the parser version can take arbitrary input form the command line or a string.

.. code-block:: python

    # equivalent to
    pandad = iris[(iris.Sepal_Length > 6) & (iris.Sepal_Width < 3)]
    print(pandad.describe())

