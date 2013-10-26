.. link: 
.. description: 
.. tags: 
.. date: 2012/10/26 14:34:48
.. title: daetools personal reminder
.. slug: daetools-personal-reminder


Note: in daetools you can't do this:

.. code-block:: python

     var.AssignValue()

if var is a differential variable.  You must create an equation for it that results in it being constant, e.g.

.. code-block:: python

     eq = self.model.CreateEquation("a","b")
     eq.Residual = self.var() - Constant(1 * unit)

