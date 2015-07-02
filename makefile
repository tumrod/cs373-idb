FILES :=                              \
    .travis.yml                       \
    .gitignore						  \
    makefile						  \
    apiary.api                 	      \
    IDB.log                           \
    models.html                       \
    models.py                         \
    test.py   	                      \
    UML.pdf

all:

check:
	@for i in $(FILES);                                         \
    do                                                          \
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
    done

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  Collatz.html
	rm -f  Collatz.log
	rm -rf __pycache__

config:
	git config -l

test: test.py

models.html: models.py
	pydoc3 -w models

IDB.log:
	git log > IDB.log


