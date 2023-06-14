#!/bin/bash
rm -rf dist/** && \
python setup.py sdist bdist_wheel && \
if python3 -m pip install dist/*.whl &2>1 > /dev/null; then
    echo "Successfully installed the package"
else
    echo "Failed to install the package"
fi && \

if python3 -m twine upload dist/* --verbose --skip-existing &2>1 > /dev/null; then
    echo "Successfully uploaded the package"
else
    echo "Failed to upload the package"
fi
```

