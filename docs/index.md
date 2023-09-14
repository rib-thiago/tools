# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


## Sobre os Estudos

One of the best practices is to write your functions’ comments and test cases first, which helps you write higher quality code while keeping the function’s various corner cases and requirements in view.

Python’s doctest tool comes in extremely handy in such situations.

We can use doctest to write tests for the code in our function by defining both the input and output values, saving us time and effort while writing top quality code.

# Introducing docstring

Python has a module named docstring. docstrings are string literals that we use in a function, class, or module declaration to write comments and test cases within our functions. Therefore, docstrings are essential for both documentation and testing purposes.

We can write a docstring between three quotes:

~~~ 
"""Following the docstring, we can write both the comments and the tests, also between three quotes."""
~~~~

At first sight, a docstring and a comment might seem similar. However, they serve different purposes. Comments explain the implementation of the code, while docstrings document classes, methods, and functions. They help other programmers understand the purpose of a function and how they can use it in their work.


The doctest module identifies a docstring within functions or class definitions for its purpose. We preface the test cases within the docstring with the symbol >>> to identify and differentiate between the comments and the test code.

The doctest module looks for and detects patterns in the docstring that look like interactive Python sessions. Once detected, the doctest executes them. The doctests must exist in the initial docstring right after the function call or method header. Make sure to avoid extra spaces after writing the doctest to avoid any unexpected errors or failures.
