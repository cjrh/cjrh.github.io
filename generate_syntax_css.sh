#!/usr/bin/env bash
# The first parameter is the name of the pygmentize theme to generate.
pygmentize -S $0 -f html > stylesheets/syntax.css
