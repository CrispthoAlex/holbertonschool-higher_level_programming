![](https://blog.holbertonschool.com/wp-content/uploads/2019/06/cherry72-942x1024.png)
# Welcome to the [Python](https://docs.python.org/3.4/tutorial/index.html) world!

After 3 months of C, you will start Python today.
The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

#### - Guillaume, CTO at Holberton

## [Python 3.4.10 Documentation](https://docs.python.org/3.4/tutorial/index.html)

Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Pythons elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

## Install PEP8

For this project will use [PEP8](https://www.python.org/dev/peps/pep-0008/) as our guide for style for Python Code

``Pycodestyle`` is now the [new standard of Python style code](https://intranet.hbtn.io/rltoken/D67mmHg2X9ZI7QHlQxayyw), but at school we will use ``PEP8, version 1.7.*`` Dont worry, ``pycodestyle`` is based on ``pep8``. The hardest part now is to install it for Python 3:

### Regular Ubuntu 14.04 install

``$ sudo apt-get install python3-pep8``

### Using Pip3
#### Install Pip3

``$ sudo apt-get install python3-pip``

Install Pep8

``$ pip3 install pep8``

Make sure you have the right version

````
$ pep8 --version
1.7
$
````

If its not the case, it means PEP8 is installed but not linked in your PATH. You should look at these folders to find where it has been installed:

* /usr/local/lib/python3*/dist-packages/pep8.py
* /usr/lib/python3*/dist-packages/pep8.py

Dont hesitate to delete /usr/bin/pep8 and replace by one of those pep8.py:

* cp pep8.py /usr/bin/pep8
* chmod u+x /usr/bin/pep8

Finally, if you cant make it work, please use the container-on-demand tool to PEP8 your files in a pre-configured container.

## Why... [Monty Python](https://es.wikipedia.org/wiki/Monty_Python)?
![](https://blogdanae.files.wordpress.com/2013/04/12.jpg?w=768&h=432)