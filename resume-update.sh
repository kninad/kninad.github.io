#!/bin/bash

Rootdir="/mnt/Study/job/resume/current-cv-resume/"

# RESUME="${Rootdir}/Resume_NinadKhargonkar.pdf"
CV="${Rootdir}/CV_NinadKhargonkar.pdf"

cp $CV ./etc/

git add ./etc/CV_NinadKhargonkar.pdf

git commit -m 'cv update'

git push origin master

