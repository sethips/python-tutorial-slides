################
Python3 Tutorial
################

The slide is powered by the framework `reveal.js`_ (Hakim El Hattab) under MIT license. Unless otherwise mentioned, the content itself is licensed under a `Creative Commons Attribution 3.0 Unported License`__.

.. _reveal.js:  https://github.com/hakimel/reveal.js/
__ http://creativecommons.org/licenses/by/3.0/


Introduction
============


Old Version Slides
==================

For old version of this version, which is powered by another framework `deck.js`_, can be found at http://ccwang002.github.io/python-tutorial-slides/old.2013.04/. However, old version slides will not be further maintained.

.. _deck.js: http://imakewebthings.com/deck.js


For Slides Uploading
====================

I manage the online slides, equivalently the ``gh-pages`` branch, using `ghp-import`_.

It can be installed using ``pip``

.. code-block:: bash

    # On Python 3.3 crashes, use Python 2.7 instead
    pip install ghp-import

To update the slides content shown in the ``gh-pages`` branch, it is simply one command away

.. code-block:: bash

    ghp-import -m 'Update slides' -p .

.. _ghp-import: https://github.com/davisp/ghp-import
