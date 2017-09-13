all: build-simulation_chi2

clean:
	rm -rf *.pdf

build-%:
	pandoc --toc --filter pandoc-citeproc --filter pandoc-eqnos $*.md -o $*.pdf
