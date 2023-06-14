#!/bin/bash
VERSION="0.2.7"
rm -rf dist/** && \
sed -e "s/version = \"[[:digit:]]\.[[:digit:]]\.[[:digit:]]\"/version = \"${VERSION}\"/g" setup.py | tee setup.temp.py && \
sed -e "s/version = \"[[:digit:]]\.[[:digit:]]\.[[:digit:]]\"/version = \"${VERSION}\"/g" setup.cfg | tee setup.temp.cfg && \
sed -e "s/version = \"[[:digit:]]\.[[:digit:]]\.[[:digit:]]\"/version = \"${VERSION}\"/g" pyproject.toml | tee pyproject.temp.toml && \
mv setup.temp.py setup.py && \
mv setup.temp.cfg setup.cfg && \
mv pyproject.temp.toml pyproject.toml

python setup.py sdist bdist_wheel && \
if python3 -m pip install dist/*.whl 2>&1 ; then
    echo "Successfully installed the package"
else
    echo "Failed to install the package"
fi

if python3 -m pytest tests/ 2>&1 ; then
    echo "Successfully ran the tests"
else
    echo "Failed to run the tests"
    exit 1
fi
python3 -m twine upload dist/* --verbose --skip-existing

