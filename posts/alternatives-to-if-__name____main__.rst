.. link: 
.. description: 
.. tags: 
.. date: 2012/12/01 17:59:00 
.. title: Alternatives to if __name__=='__main__':
.. slug: alternatives-to-if-__name____main__

So I find this irritating:

.. code-block:: python

    def main():
        print('Hello')

    if __name__=='__main__':
        main()

I played around a bit and ended up with something that lets one do this:
from mainfunc import main

.. code-block:: python

    @main
    def runme():
        print('runme')

    def norunme():
        print('norunme')

When this script is run, "runme" is printed, but not "norunme".  Anyone guess
what mainfunc.main() looks like? (By the way, my implementation doesn't work
properly, but it's just a thought experiment for now).

