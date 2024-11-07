from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pytest-cleanuptotal',
    packages=find_packages(where='src', exclude=['*tests*']),
    package_dir={'': 'src'},
    version='0.3.5',
    author='Tzur Paldi',
    author_email='tzur.paldi@outlook.com',
    maintainer='Tzur Paldi',
    maintainer_email='tzur.paldi@outlook.com',
    license='MIT',
    url='https://github.com/tzurp/pytest_cleanuptotal',
    description='A cleanup plugin for pytest',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Pytest",
    ],
    entry_points={
        'pytest11': [
            'pytest_cleanuptotal = pytest_cleanuptotal.cleanuptotal',
        ],
    },
)
