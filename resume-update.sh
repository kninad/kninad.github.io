#!/bin/bash

Rootdir="/mnt/Study/job/resume/current-cv-resume/"

RESUME="${Rootdir}/Resume_NinadKhargonkar.pdf"

cp $RESUME ./etc/

git add ./etc/Resume_NinadKhargonkar.pdf

git commit -m 'resume update'

git push origin master

