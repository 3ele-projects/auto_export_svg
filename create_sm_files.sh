#!/bin/bash

file_path="$PWD"
#mkdir logoexportsm
#sudo    apt-get install python3-venv

python3 -m venv $file_path
source $file_path/bin/activate
pip3 install -r requirements.txt

python3 main.py $1 $2 "$file_path"
#cp *.png logoexportsm
#cd logoexportsm
#zip export.zip *
#echo "done"


