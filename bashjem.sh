#!/bin/bash

for jemfile in ./*.jemdoc
do
	filename="${jemfile%.*}"
	echo "Converting $jemfile to $filename.html"
	jemdoc $jemfile
done
