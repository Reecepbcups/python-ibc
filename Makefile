# update version in setup.py

# https://github.com/jinhangjiang/Your-First-Python-Package-on-PyPI
all: clean build-py install

clean:
	@rm -rf build/ dist/
	@echo "Cleaned up"

build-py:	
	@python setup.py build sdist bdist_wheel

install:
	@python -m pip install dist/*-*.tar.gz

upload:
	# https://packaging.python.org/en/latest/tutorials/packaging-projects/
	# python3 -m twine upload --repository cosmpy-api dist/*
	twine upload --repository pypi dist/*

version:
	@pip show python-ibc