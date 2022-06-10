from setuptools import find_packages, setup

setup(
    name='whatif',
    packages=find_packages("src"),
    package_dir={"": "src"},
    version='0.1.0',
    description='Project packaging Python code for Excel "what if?" type analysis',
    author='Dimas Moosa',
    license='',
)
