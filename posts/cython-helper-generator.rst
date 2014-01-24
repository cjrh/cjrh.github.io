.. link: 
.. description: 
.. tags: 
.. date: 2012/11/27 16:46:49
.. title: Cython helper generator
.. slug: cython-helper-generator

I call this makeext.py.  You call it like so:

.. code-block::

    makeext.py helloworld.pyx module1.pyx module2.pyx

or

.. code-block::

    makeext.py *.pyx

and it converts all the given pyx files into pyd binary modules.  Basically, no
setup.py intermediate is required. This is great for small utility-type
applications, but will obviously not be suitable for more complex and
specialized builds.

The code:


.. code-block:: python

    import sys
    import os
    from os.path import splitext

    if len(sys.argv) == 1:
        print 'You must supply one or more .pyx filenames.'
        sys.exit()

    if sys.argv[1].lower() == '*.pyx':
        files = os.listdir('.')
    else:
        files = sys.argv[1:]
    extensions = [(splitext(f)[0], f) for f in files if splitext(f)[1].lower() == '.pyx']

    # No pyx files given.
    if len(extensions) == 0:
        print 'No .pyx filenames were supplied.  Exiting.'
        sys.exit()

    # Checking for missing files
    missing = [f for n, f in extensions if not os.path.exists(f)]
    if missing:
        print 'One or more given files were missing:'
        for f in missing:
            print '    {}'.format(f)
        print 'Aborting.'

    # Restore distutils command line args
    sys.argv = [sys.argv[0], 'build_ext', '--inplace']

    from distutils.core import setup
    from distutils.extension import Extension
    from Cython.Distutils import build_ext

    setup(
        cmdclass = {'build_ext': build_ext},
        ext_modules = [Extension(n, [f]) for n, f in extensions]
    )

    # Cleanup: delete intermediate C files.
    for n, f in extensions:
        if os.path.exists(n+'.c'):
            os.remove(n+'.c')

