####################
IS 210 Assignment 08
####################
******************
Synthesizing Tasks
******************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Points: 18
:Due-Date: YYYY-MM-DDTHH:mm:ss

Overview
========

These synthesizing tasks will use a combination of all the tools thus-far
encountered to create some interesting basic programs.

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Synthesizing Tasks
==================

Task 01
-------

In this task, we're going to be creating a list of versus matchups for players
in a [*insert your favorite two-player game here*] tournament. This is a
surprisingly simple task for programs to accomplish for groups of players of
any size from two to millions.

To acheive this objective we're going to use a nested ``for`` loop and,
specifically, loop over the *same* object twice to produce what's known as a
*Cartesian Product*. A full Cartesian Product is like a table with the same
rows and columns, eg:

.. table:: Full Cartesian

    ========= ======== ======== ======== ========
    Players   Player 1 Player 2 Player 3 Player 4
    ========= ======== ======== ======== ========
    Player 1  Yes      Yes      Yes      Yes
    Player 2  Yes      Yes      Yes      Yes
    Player 3  Yes      Yes      Yes      Yes
    Player 4  Yes      Yes      Yes      Yes
    ========= ======== ======== ======== ========

In other words, the length of a full Cartesian Product is ``n ** 2`` where
``n`` is the number of items in the original object.

For a matchups scenario, however, this is unideal because it not only sets up
a situation where Player 1 might be facing Player 1 (an impossible condition),
but it also causes double-matches where Player 1 (the row) faces Player 2 (the
column) and later, Player 2 (the row) places Player 1 (the column). So,
instead, the type of matchup we desire is what we refer to as a
Half-Cartesian, or, in tabular form:

.. table:: Half Cartesian

    ========= ======== ======== ======== ========
    Players   Player 1 Player 2 Player 3 Player 4
    ========= ======== ======== ======== ========
    Player 1  No       Yes      Yes      Yes
    Player 2  No       No       Yes      Yes
    Player 3  No       No       No       Yes
    Player 4  No       No       No       No 
    ========= ======== ======== ======== ========

In the above example, each player interacts with each other player only once.
Now, interestingly enough, achieving this Half-Cartesian does not require
particularly complex checking, in-fact, these all have a mathematical
relationship if you consider the *index* of each of these items in a list. As
above, the index of the row must always be less than the index of a column.

Specifications
^^^^^^^^^^^^^^

1.  Create a module named ``task_01.py``

2.  In ``task_01.py`` create a new function named ``get_matches()`` that takes
    exactly one argument:

    1.  ``players`` (list): A list of player names.

        .. code:: python

            ['James', 'Jesse', 'Jennifer']

3.  Process the list of names to produce a new list of unique matchups between
    players stored as a list of tuples.

4.  Return the newly created list of tuples.


.. important::

    As a good exercise for you, I want you to solve this problem without the
    use of a counter.

.. hint::

    Brush up on the ``enumerate()`` function and how you can use it.
  
Examples
^^^^^^^^

If you're looking for a good source of test data, feel free to use the
supplied ``data`` module and the ``VERSUS`` constant found within it.

.. code:: pycon

    >>> import task_01
    >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
    [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]

.. important::

    Depending upon how you chose to compare and loop your inputs the order of
    your items may not match the above. That is a-ok as tests this week are
    designed to ignore order and are merely examining content. As long as your
    matchups remain unique your tests should execute cleanly.

Task 02
-------

In this exercise, you'll be implementing something that resembles the structure
of a login or authentication screen. Many login systems will give you a few
attempts before locking you out. Our system does something similar.

Using ``getpass.getpass()`` you'll be prompting users to provide their
passwords which will then be hashed and compared against the stored hash. As a
subject password hashing and salting are a bit beyond the scope of our course
but if you're curious for an act-alike, take a look inside the included
``authentication`` package, and notably ``__init__.py``.

The ``USERS`` constant provides a simplified dictionary of users with their
salts and hashed passwords. Because it's insecure to store passwords in
plaintext, we always store them as one-way hashes. I note that this isn't the
same idea as encryption since an encrypted passphrase could be decoded with the
right key.  A hash is, instead, something that consistently scrambles an output
but may not be unscrambled so even a system owner couldn't peek at users'
passwords. 

You may be wondering if, since the passwords are permanently hashed, how we
can compare them to know if the right password was entered. Direct your
attention towards ``authentication.authenticate()``. The reason this works
is because we can hash the user input in the exact same way and compare the
two hashes without "knowing" the original passphrase.

Pretty neat, huh?

.. important::

    It's important to note that while such a solution could indeed provide a
    base for such a system, you should not use this solution, unaltered, in any
    production context as this implementation is incomplete.

Specifications
^^^^^^^^^^^^^^

1.  Create a new module named ``task_02.py``

2.  In ``task_02.py``, import the ``authentication`` package and the
    ``getpass`` module.
    
    The ``getpass.getpass()`` method works just like
    ``raw_input()`` with the exception of not printing what it typed onto the
    screen which makes it more secure for entering passwords. To see how it
    works, try:

    .. code:: pycon

        >>> import getpass
        >>> myval = getpass.getpass('A prompt?')
        A prompt?

    Type anything you want after ``A prompt?`` and hit *Enter*. Now, check
    ``myval``

    .. code:: pycon

        >>> print myval

3.  Create a new function in ``task_02``, naMED ``login()`` that takes two
    parameters, in order:

    1.  ``username`` (str): A string representing the username of the user
        attempting to log in

    2.  ``maxattempts`` (int, optional): An integer represent the maximum
        number of prompted attempts before the function returns False. Defaults
        to ``3``

4.  Near the top of the function create a variable to store whether or not the
    user has been authenticated and set its value to ``False``. This will be
    the variable you return at the end of the function and is a technique known
    as *defensive programming*. In this technique we always assume the most
    pessimistic stance possible (``False``) until we have a reason to set
    it otherwise. Designing your programs around such a paradigm is always a
    good idea!

5.  Using a ``while`` loop, use a combination of ``getpass.getpass()`` and
    ``authentication.authenticate()`` to prompt the end-user for a password
    and determine whether or not the correct password was received. If a user
    submits an incorrect password they should be prompted again until they have
    exceeded their max attempts. A message should notify a user if they
    submitted incorrectly and the number of attempts left. Look at the
    documentation for ``authentication.authenticate()`` on how to use it.

    Leave the third parameter of ``authentication.authenticate()`` as its
    default value.

6.  Return ``True`` if the user has successfully authenticated before hitting
    the maximum number of attempts or ``False`` if they exceed that maximum
    number of failed attempts.

.. tip::

    Your various printed statements and prompts are something that you don't
    need to continually redeclare inside your loop. You can declare them once,
    outside your loop, and reference them internally.

.. hint::

    You are being introduced to several new tools in this task. Don't try to
    do everything all at once. Instead use each tool in isolation in the
    python console (``>>>``) to get a feel for how it works. After you feel
    comfortable start putting the pieces together one at a time and testing
    them individually.

Examples
^^^^^^^^

The following table lists the current database of users and their plaintext
passwords (to be used for testing).

.. table:: Users

    ========== =============
    Username   Password
    ========== =============
    augustus   food
    charlie    kindness
    mike       television
    veruca     greed
    violet     gum
    ========== =============

.. note::

    You must do your testing on the terminal. ``getpass.getpass()`` will
    **not** prompt you in the idle console window.

The following simulates a number of failed attempts in excess of the maximum
attempts.

.. code:: pycon

    >>> import task_02
    >>> task_02.login('mike', 4)
    Please enter your password:
    Incorrect username or password. You have 3 attempts left.
    Please enter your password:
    Incorrect username or password. You have 2 attempts left.
    Please enter your password:
    Incorrect username or password. You have 1 attempts left.
    Please enter your password:
    Incorrect username or password. You have 0 attempts left.
    False

The next example simulates an initial failed attempt followed by a successful
attempt.

.. code:: pycon

    >>> import task_02
    >>> task_02.login('veruca', 2)
    Please enter your password:
    Incorrect username or password. You have 1 attempts left.
    Please enter your password:
    True

Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ bash runtests.sh

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Week Two.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
