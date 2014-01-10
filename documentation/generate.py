import os
import sys

root_dir = '.'
doc_dir=os.path.join(root_dir,'documentation')
header = os.path.join(doc_dir,'header.html')
footer = os.path.join(doc_dir,'footer.html')

#for all files...
for folder, subs, files in os.walk(root_dir):
    for filename in files:
        #that end with the markdown extension
        if filename.endswith('.md'):
            md_file = os.path.join(folder,filename)

            #replace the code (using a tmp file)
            print("processing", md_file)
            tmp_file = md_file + '.tmp'
            with open(tmp_file, 'w') as dest:
                with open(md_file, 'r') as src:
                    for line in src:
                        #if we find an include
                        if line.startswith('***'):
                            prog_file = line.replace('***','').strip()
                            prog_file = os.path.join(folder,prog_file)
                            #replace it with all the lines of the file
                            with open(prog_file) as prog_src:
                                dest.write('~~~ {.prettyprint .linenums}\n')
                                for line in prog_src:
                                    dest.write(line)
                                dest.write('~~~\n')

                        #otherwise just copy the line
                        else:
                            dest.write(line)
            
            #for html output
            #process the markdown file with pandoc
            html_file = md_file + '.html'
            os.system("pandoc -s -S --indented-code-classes='prettyprint linenums' -H %s -A %s %s -o %s" % ( header, footer, tmp_file, html_file))
            #how to do pagination for pdfs? but still make them look good?
            #os.system("pandoc --toc -N -s -S --indented-code-classes='prettyprint linenums' -H %s -A %s %s -o %s" % ( header, footer, tmp_file, html_file))


            #make pdfs
            pdf_file = md_file + '.pdf'
            os.system("wkhtmltopdf %s %s" % (html_file, pdf_file))
            
            #remove the tmp file
            os.remove(tmp_file)
