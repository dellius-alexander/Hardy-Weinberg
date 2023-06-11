#!/bin/bash

python setup.py sdist bdist_wheel && \
python3 -m twine upload dist/* --verbose --skip-existing

