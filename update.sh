#!/bin/bash

#generate docs
echo "generate docs"
./documentation/generate.py  --verbose

#update zip
echo "updating zip"
cd reaction_timer
zip reactiontimer.zip *pdf ../glossary.pdf ../cheatsheet.pdf

#make tar.gz
echo "creating tar"
cd ../../
tar -czf piffin.tar.gz lab-kit/

#copy to server
echo "copying to piffin.co.uk"
scp piffin.tar.gz  matt@mattvenn.net:/tmp/
