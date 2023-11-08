# Example Package

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

We followed this [packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)


Packaging with editable build:
1. Quick tutorial packaging toml: https://packaging.python.org/en/latest/tutorials/packaging-projects/
2. Link to git of the afore example: https://github.com/pypa/sampleproject/tree/main The example is a newer version of the tutorial - the tutorial is not updated 
3. detailed instructions on packaging and distributing files: https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
    1. You will find the build editable here! : https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#working-in-development-mode
        1. in terminal: "pip install -e ." from the root directory of the project
4. Necessary update of pip (greater >21 I think) so that pip install -e . is supported 
https://stackoverflow.com/questions/69711606/how-to-install-a-package-using-pip-in-editable-mode-with-pyproject-toml

Simply run in terminal pytest for pytests: pytest

Install pytest coverage if not present: pip install pytest-cov

Then produce html reports: python -m pytest --cov=example_package_annteli --cov-report=html
