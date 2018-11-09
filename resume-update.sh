#!/bin/bash

Rootdir="/mnt/Study/job/resume/current-cv-resume/"

CV="${Rootdir}/CV_NinadKhargonkar.pdf"
RES="${Rootdir}/Resume_NinadKhargonkar.pdf"

cp $CV ./etc/
cp $RES ./etc/

git add ./etc/CV_NinadKhargonkar.pdf ./etc/Resume_NinadKhargonkar.pdf
git commit -m 'cv-resume update'
git push origin master

