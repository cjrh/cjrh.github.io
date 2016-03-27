#!/usr/bin/env bash
# The first parameter is the name of the pygmentize theme to generate.
# e.g. bw, monokai, github, rrt, perldoc, manni, borland, colorful, default,
# murphy, vs, trac, tango, fruity, autumn, emacs, vim, pastie, friendly,
# native.
# The second parameter is the output "syntax.css" file to create.
pygmentize -S $0 -f html > $1
