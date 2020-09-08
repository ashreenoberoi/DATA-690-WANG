# Course Notes 


### Why do we use python? 
It can be used to write quick-and-dirty small programs,or scripts.The main Python language advantages are that it is easy to read and easy to learn. It is easier to write a program in Python than in C or C++. With this language, I gain the possibility to think clearly while coding, which also makes the code easier to sustain.


### Why not Python?
>>Python is slower as compared to C, C++ and Java.
>>>Python’s memory consumption is also high, due to the flexibility of the data types.
>>>>One of the major drawbacks of this language is that its design has numerous issues. Python programmers face several issues regarding the design of the language. This language requires more testing and also it has errors that only show up at runtime this is because the language is dynamically typed


### NumPy: 
NumPy contains a multi-dimensional array and matrix data structures. It can be utilised to perform a number of mathematical operations on arrays such as trigonometric, statistical, and algebraic routines. You can use it to find basic mathematical operations like mean , median, mode, range and standard diviation. The syntax is extremely simple and with one line codes you can find all the answers.


### Pandas: 
Pandas helps us to manipulate data. From reading a csv to writing in it , cleaning the data and combining various csvs. It came into existance for  for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.


### Matplotlib:
matplotlib is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc. In matplotlib various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes. 


### SciPy: 
SciPy open-source Python library used for scientific computing and technical computing. SciPy builds on the NumPy array object and is part of the NumPy stack which includes tools like Matplotlib, pandas and SymPy, and an expanding set of scientific computing libraries.


### scikit-learn: 
Scikit-learn is a free machine learning library for Python. It features various algorithms like support vector machine, random forests, and k-neighbours, and it also supports Python numerical and scientific libraries like NumPy and SciPy

### How to import Libraries : 
>>>import numpy as 
>>>>np import pandas as pd 
>>>>import matplotlib.pyplot as plt import urllib


### How to read txt file: 
>>>path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt' and print open(path).readline()


### Counting time zone in pure python: 
>>>time_zones = [rec['tz'] for rec in records if 'tz' in rec] and printing it time_zones[:10]


### Counting time zone in pandas : 
>>>from pandas import DataFrame, Series
>>>>import pandas as pd  
>>>>>frame = DataFrame(records)
>>>>>>frame


### Basic python commands : 
>>>print "Hello, Python!"


# Writing comments : 
>>>!/usr/bin/python # First comment print "Hello, Python!" # second comment
>>>>Python string commands: str = 'Hello World!'
>>>>>print str          # Prints complete string
>>>>>>print str[0]       # Prints first character of the string
>>>>>>>print str[2:5]     # Prints characters starting from 3rd to 5th
>>>>>>>>print str[2:]      # Prints string starting from 3rd character
>>>>>>>>>print str * 2      # Prints string two times
>>>>>>>>>>print str + "TEST" # Prints concatenated strin


### The %run Command
You  can  run  any  file  as  a  Python  program  inside  the  environment  of  your  IPythonsession using the %run command. 
Suppose you had the following simple script storedin ipython_script_test.py:
>>>def f(x, y, z):
>>>>return (x + y) / za = 5b = 6c = 7.5
>>>>>result = f(a, b, c)
You can execute this by passing the filename to %run:
>>> %run ipython_script_test.py


### About Magic Commands
IPython’s  special  commands   are  known  as“magic” commands. These are designed to facilitate common tasks and enable you toeasily  control  the  behavior  of  the  IPython  system.  A  magic  command  is  any  com‐mand  prefixed  by  the  percent  symbol  %.  
For  example,  you  can  check  the  executiontime  of  any  Python  statement,  such  as  a  matrix  multiplication,  using  the  %timeitmagic function 
>>>a = np.random.randn(100, 100)
>>>>%timeit np.dot(a, a)


### Imports 
In  Python  a  module  is  simply  a  file  with  the  .py  extension  containing  Python  code.

Most  objects  in  Python,  such  as  lists,  dicts,  NumPy  arrays,  and  most  user-definedtypes (classes), are mutable. This means that the object or values that they contain canbe modifiedThe primary Python types for numbers are int and float. An int can store arbitrar‐ily large numbers. Floating-point numbers are represented with the Python float type. Under the hoodeach one is a double-precision (64-bit) value. They can also be expressed with scien‐tific notation.


### Strings
Many people use Python for its powerful and flexible built-in string processing capa‐bilities. You can write string literals using either single quotes ' or double quotes ":a = 'one way of writing a string'b = "another way"For multiline strings with line breaks, you can use triple quotes, either ''' or """


### Bytes and UnicodeIn modern Python 
Unicode has become the first-class stringtype to enable more consistent handling of ASCII and non-ASCII text. In older ver‐sions  of  Python,  strings  were  all  bytes  without  any  explicit  Unicode  encoding.  Youcould convert to Unicode assuming you knew the character encoding. 


### Booleans 
Two boolean  values  in  Python  are  written  as  True  and  False.  Comparisons  andother  conditional  expressions  evaluate  to  either  True  or  False.  Boolean  values  arecombined with the and and or keywords.

### Tuples
In Python, variables can be grouped together under one name. There are different ways to do this,and one is to use tuples. Tuples make sense for small collections of data, e.g. for coordinates:
>>>(x,y) = (5, 3)
>>>>oordinates = (x,y)
>>>>>print coordinates

### Lists (arrays)
Lists are ordered sequences of objects.It can for example be very practical to put many measured values, or names of an address book, into a list, so they can be accessed by one common name. 
>>>nameslist = ["Sam", "Lisy", "Pit"]
>>>>numberslist = [1, 2, 3.14]
>>>>>mixedlist = ["ham", 'eggs', 3.14, 5]

### Range: 
Producing lists of integer numbers.Often you need a regularly spread list of numbers from a beginning value to an end value. This is done by the range function:
>>>r1 = range(11) # 0...10
>>>>print r1 # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

### Functions
It is a good idea to put pieces of code that do a clearly defined task into separate blocks that are called functions. Functions must be defined before they are used.Once they are defined, they can be used like native Python statements.A very simple example calculates area and perimeter of a rectangle:

function definitions
>>>def area(b, h):
 
""" calculate area of a rectangle"""
 >>>>A = b * h
 
>>>>>return A



