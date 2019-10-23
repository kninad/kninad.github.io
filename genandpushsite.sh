#!/bin/bash

jemdoc -c mysite.conf *.jemdoc.txt

git add .
git commit -m 'generate and push'
git push origin master


