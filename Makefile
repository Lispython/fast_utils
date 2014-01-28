
all: clean-pyc test

docs:
	cd docs && make html

test:
	python setup.py test

travis:
	py.test tests/


shell:
	../venv/bin/ipython

audit:
	python setup.py autdit

version := $(shell sh -c "grep -oP 'VERSION = \"\K[0-9\.]*?(?=\")' ./setup.py")

build:
	python setup.py sdist

release: clean-pyc
	git tag -f v$(version) && git push --tags
	python setup.py sdist upload

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean: clean-pyc
	find . -name '*.egg' -exec rm -rf {} +

find-print:
	grep -r --include=*.py --exclude-dir=venv --exclude=fabfile* --exclude=tests.py --exclude-dir=tests --exclude-dir=commands 'print' ./

activate:
	. venv/bin/activate

env:
	./buildenv.sh
	. venv/bin/activate
