#!/bin/bash

# By Chris Albon
# March 4, 2015

# This script activates a python 3.x environment called py3k and then
# converts a single iPython Notebook files to basic html.

source activate py3k

cd "$(dirname "$0")"

ipython nbconvert --to html --template basic pandas_normalize_column.ipynb

