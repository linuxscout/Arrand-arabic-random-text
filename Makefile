#/usr/bin/sh
# Build Arrand: random Arabic text generator

default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all: install install3 wheel wheel3  doc
# Publish to github
publish:
	git push origin master 

md2html:
	pandoc -s -r markdown -w html README.md -o README.html
	
wheel:
	sudo python3 setup.py bdist_wheel

upload:
	echo "use twine upload dist/arrand-0.1.tar.gz"

test:
	python3 -m unittest discover tests
docs:
	epydoc -v --config epydoc.conf
dev:
	pip install -e .

cli:
	python -m arrand                          # Default (random text)
	python -m arrand --category aya          # One random aya
	python -m arrand -c poem -n 3            # Three random poems
	python -m arrand -c phrase --vocalized   # Vocalized phrase
	python -m arrand -c nonsense -n 2        # Nonsense lines
