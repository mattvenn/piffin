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
    
    #substitute code, hardcoded for now 
    sed -e '/^reaction.py/ {                               
    r reaction.py
    d }' < README.md > README.md.tmp

    pandoc -s -S --indented-code-classes='prettyprint linenums' -c $doc/pandoc.css -H $doc/header.html -A $doc/footer.html $file.tmp -o $file.html
#    wkhtmltopdf $file.html $file.pdf

    #remove the tmp file
    rm README.md.tmp
    cd $root
done
