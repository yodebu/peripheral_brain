#!/bin/bash

# By Chris Albon
# March 4, 2015

# This script activates a python 3.x environment called py3k, sets the current
# working directory to the directory the file is currently in and then
# converts all iPython Notebook files to basic html.

source activate py3k

cd "$(dirname "$0")"

for f in *.ipynb; do ipython nbconvert --to html --template basic $f; done

