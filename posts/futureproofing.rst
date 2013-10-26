.. link: 
.. description: 
.. tags: 
.. date: 2012/08/27 15:52:38
.. title: Futureproofing
.. slug: futureproofing

In preparation for transition from Python 2.7 to Python 3.x, it is a really
good idea to set up your editor so that the template for new python modules
carries this line at the top by default:

.. code-block:: python

    from __future__ import absolute_import, division, print_function, unicode_literals


