autogenerate docs with this:

    pandoc -s -S --toc -c pandoc.css -A footer.html README.md quizbuttons/README.md reactiontester/README.md -o example3.pdf
