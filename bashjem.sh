#!/bin/bash

Dir="."

for jemfile in $Dir/*.jemdoc
do
    filename="${jemfile%.*}"
    echo "Converting $jemfile to $filename.html"
    jemdoc -o $filename.html $jemfile
done


