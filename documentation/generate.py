import os
import sys

root_dir = os.path.realpath(os.curdir)
doc_dir=os.path.join(root_dir,'documentation')
header = os.path.join(doc_dir,'header.html')
footer = os.path.join(doc_dir,'footer.html')
template = os.path.join(doc_dir,'template.tex')
css = os.path.join(doc_dir,'pandoc.css')

#for all files...
for directory, subs, files in os.walk(root_dir):
    os.chdir(root_dir)
    for filename in files:
        #that end with the markdown extension
        if filename.endswith('.md'):
            if not directory.endswith('reactiontester'):
                print("ignoring " + directory )
                continue
            else:
                print("processing files in " + directory)

            #move to that dir
            os.chdir(directory)
            md_file = filename

            #replace the code (using a tmp file)
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
            print("making " + html_file)
            #these options make pandoc assume --standalone which is why the css for the syntax highlighting happens
            os.system("~/.cabal/bin/pandoc -H %s -A %s %s -o %s" % ( header, footer, tmp_file, html_file))

            #make pdfs
            pdf_file = md_file + '.pdf'
            #fonts work with xelatex
            print("making " + pdf_file)
            os.system('~/.cabal/bin/pandoc  --template=%s --variable mainfont="DejaVu Sans" --variable sansfont="DejaVu Sans" --variable fontsize=12pt --latex-engine=xelatex %s --toc -o %s'% ( template,tmp_file,pdf_file))
            
            #remove the tmp file
            os.remove(tmp_file)
