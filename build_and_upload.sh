#!/bin/bash
VERSION="0.3.1"
rm -rf dist/** && \
sed -e "s/version = \"[[:digit:]]\.[[:digit:]]\.[[:digit:]]\"/version = \"${VERSION}\"/g" setup.py | tee setup.temp.py && \
sed -e "s/version = \"[[:digit:]]\.[[:digit:]]\.[[:digit:]]\"/version = \"${VERSION}\"/g" setup.cfg | tee setup.temp.cfg && \
mv setup.temp.py setup.py && \
mv setup.temp.cfg setup.cfg && \
mv pyproject.temp.toml pyproject.toml

if python3 -m pytest tests/ 2>&1 && python setup.py sdist bdist_wheel 2>&1 ; then
    echo "Build and test ran Successfully."
else
    echo "Failed to run the tests"
    exit 1
fi

#python3 -m twine upload dist/* --verbose --skip-existing
#python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose --skip-existing
#if python3 -m pip install hardyweinbergcalculator 2>&1 ; then
#    echo "Successfully installed the package"
#else
#    echo "Failed to install the package"
#fi
