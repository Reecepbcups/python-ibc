
rm -r build/ dist/
python setup.py sdist bdist_wheel
python -m pip install dist/cosmpy-api-*.tar.gz
# https://github.com/jinhangjiang/Your-First-Python-Package-on-PyPI