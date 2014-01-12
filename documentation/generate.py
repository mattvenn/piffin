#!/usr/bin/python
import os
import sys
import argparse

root_dir = os.path.realpath(os.curdir)
doc_dir=os.path.join(root_dir,'documentation')
header = os.path.join(doc_dir,'header.html')
footer = os.path.join(doc_dir,'footer.html')
template = os.path.join(doc_dir,'template.tex')
css = os.path.join(doc_dir,'pandoc.css')

def process(md_file):
    #replace the code (using a tmp file)
    if args.verbose:
        print("pre-processing", md_file)
    tmp_file = md_file + '.tmp'
    with open(tmp_file, 'w') as dest:
        with open(md_file, 'r') as src:
            for line in src:
                #if we find an include
                if line.startswith('***'):
                    prog_file = line.replace('***','').strip()
                    #replace it with all the lines of the file
                    with open(prog_file) as prog_src:
                        dest.write('~~~ {.python .numberLines}\n')
                        for line in prog_src:
                            dest.write(line)
                        dest.write('~~~\n')

                #otherwise just copy the line
                else:
                    dest.write(line)
    
    #for html output
    #process the markdown file with pandoc
    html_file = md_file + '.html'
    if args.verbose:
        print("making " + html_file)
    #these options make pandoc assume --standalone which is why the css for the syntax highlighting happens
    os.system("~/.cabal/bin/pandoc -H %s -A %s %s -o %s" % ( header, footer, tmp_file, html_file))

    #make pdfs
    if not args.nopdf:
        pdf_file = md_file + '.pdf'
        #fonts work with xelatex
        if args.verbose:
            print("making " + pdf_file)
        os.system('~/.cabal/bin/pandoc  --template=%s --variable mainfont="DejaVu Sans" --variable sansfont="DejaVu Sans" --variable fontsize=12pt --latex-engine=xelatex %s --toc -o %s'% ( template,tmp_file,pdf_file))
        
    #remove the tmp file
    os.remove(tmp_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
    """
    create html and pdf from markdown using pandoc.
    by default will process all .md files in all sub directories.
    """)

    parser.add_argument('--verbose',
        action='store_const', const=True, dest='verbose', default=False,
        help="verbose")
    parser.add_argument('--no-pdf',
        action='store_const', const=True, dest='nopdf', default=True,
        help="don't make pdf")
    parser.add_argument('--file', action='store', dest='file', help="single file to open")

    args = parser.parse_args()

    if args.file:
        directory = os.path.dirname(args.file)
        if os.path.isdir(directory):
            os.chdir(directory)
        process(os.path.basename(args.file))
    else:
        #for all files...
        for directory, subs, files in os.walk(root_dir):
            os.chdir(directory)
            for filename in files:
                #that end with the markdown extension
                if not filename.endswith('.md'):
                    continue

                #move to that dir
                process(filename)
