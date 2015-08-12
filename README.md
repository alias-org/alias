# ALIAS 0.1

* [About](#about)

* [Installation](#installation)

* [Dependencies](#dependencies)

* [Testing](#testing)

* [Example](#example)

* [References](#references)

## About
ALIAS is a Python library for creating and manipulating [Abstract Argumentation Frameworks](https://en.wikipedia.org/wiki/Argumentation_framework) (AAF).  ALIAS 0.1 supports reading in and out from a variety of formats including databases and supports the evaluation of Argumentation Frameworks using Dung's [1] Abstract Argumentation Semantics.  

## Installation
Grab the source from githhub and install from the resulting tree:
```
$ git clone https://github.com/alias-org/alias.git
$ cd /alias
$ python setup.py install
```
## Dependencies
There are no mandatory dependencies for ALIAS, however for additional functionality some are required.  These additional dependencies are listed below:

*	Input/Output[inout]
	1. pyparsing - For file input and output.
	2. networkx - For conversion to and from NetworkX graphs and for output using matplotlib.
*	Databases[db]
	1. sqlalchemy - For interaction with SQL based database input and output.
	2. py2neo - For interaction with neo4j graph databases.
*	Testing
	1. nose - Nose testing suite.

## Testing
Unit testing requires nose (run from the alias package root):
`$ nosetests alias`

## Example
To create a blank AAF:
```
import alias
framework = alias.ArgumentationFramework('Example')
```
Add some arguments:
`framework.add_argument(['a','b'])`

And an attack:
`framework.add_attack(('a','b'))`

## References
[1] Phan Minh Dung, On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games, Artificial Intelligence, Volume 77, Issue 2, September 1995, Pages 321-357   
