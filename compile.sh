#!/usr/bin/env bash

# Clean the generated files
make clean

# Gen base level html
make all
# This will also gen some unformatted blog files

cd blog
make clean
make all