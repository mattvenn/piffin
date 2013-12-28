#!/bin/bash
root=$PWD
doc=$root/documentation
#for each markdown file:
find . -name '*md' | while read path; do
    #get the dir and file
    dir=$(dirname $path)
    file=$(basename $path)
    #change to the dir
    cd $dir
    echo "processing $path"
    #and use pandoc to generate a pdf
#    pandoc -s -S --toc $file -o $file.html
    pandoc -s -S -c $doc/pandoc.css -A $doc/footer.html $file -o $file.html
    wkhtmltopdf $file.html $file.pdf
    cd $root
done
