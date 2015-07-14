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
	rm -f  models.html
	rm -f  IDB.log
	rm -rf __pycache__

config:
	git config -l

test: tests.py
	coverage3 run    --branch tests.py >  tests.out 2>&1
	coverage3 report --omit=*site-packages* -m  >> tests.out
	cat tests.out

models.html: models.py
	pydoc3 -w models

IDB.log:
	git log > IDB.log



