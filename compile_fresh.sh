#!/usr/bin/env bash

# Clean the generated files
make clean

# Generate the html files
make all

# Git commit and push
git add .
git commit -m "website update"
git push