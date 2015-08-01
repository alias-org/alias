# ALIAS 0.1

* [About](#about)

* [Installation](#installation)

* [Example](#example)

* [References](#references)

## About
ALIAS is a Python library for creating and manipulating [Abstract Argumentation Frameworks](https://en.wikipedia.org/wiki/Argumentation_framework) (AAF).  ALIAS 0.1 supports reading in and out from a variety of formats including databases and supports the evaluation of Argumentation Frameworks using Dung's [1] Abstract Argumentation Semantics.  

## Installation
Grab the source and simply run `python setup.py install`.  This will install the library and pull any mandatory dependencies.

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