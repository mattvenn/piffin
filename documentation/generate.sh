#!/bin/bash
root=$PWD
#for each markdown file:
find . -name '*md' | while read path; do
    #get the dir and file
    dir=$(dirname $path)
    file=$(basename $path)
    #change to the dir
    cd $dir
    echo "processing $path"
    #and use pandoc to generate a pdf
    pandoc -s -S --toc $file -o $file.pdf
    cd $root
done
