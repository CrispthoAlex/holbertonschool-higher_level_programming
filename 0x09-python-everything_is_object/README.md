# 0x09. Python - Everything is object
![](https://miro.medium.com/max/670/1*LiPDcnlE8izSpz2rkXZOHA.jpeg)
# Background Context
Now that we understand that everything is an object and have a little bit of knowledge, lets pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

````
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
````

OK. But what about this?
````python
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>
````

# Resources
#### Read or watch:

* [9.10. Objects and values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
* [9.11. Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
* [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
* [Mutation (Only this chapter)](http://composingprograms.com/pages/24-mutable-data.html#sequence-objects)
* [9.12. Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
* [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* Why Python programming is awesome (dont forget to tweet today, with the hashtag #pythoniscool :))
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions

# Requirements
## Python Scripts
* Allowed editors: ``vi, vim, emacs``
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly ``#!/usr/bin/python3``
* A ``README.md`` file, at the root of the folder of the project, is mandatory
* Your code should use the ``PEP 8`` style (``version 1.7.*``)
* All your files must be executable
* The length of your files will be tested using ``wc``

## ``.txt`` Answer Files
* Only one line
* No Shebang
* All your files should end with a new line

# More Info
# Manual QA Review
* It is your responsibility to request a review for your blog from a peer before the projects deadline. If no peers have been reviewed, you should request a review from a TA or staff member.