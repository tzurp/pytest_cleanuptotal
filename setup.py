from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pytest-cleanuptotal',
    packages=find_packages(where='src', exclude=['*tests*']),
    package_dir={'': 'src'},
    version='0.3.7',
    author='Tzur Paldi',
    author_email='tzur.paldi@outlook.com',
    license="Apache-2.0",
    url="https://github.com/tzurp/pytest_cleanuptotal",
    project_urls={
        "Bug Tracker": "https://github.com/tzurp/pytest_cleanuptotal/issues",
        "Documentation": "https://github.com/tzurp/pytest_cleanuptotal#readme",
        "Source Code": "https://github.com/tzurp/pytest_cleanuptotal"
    },
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        # You can add other classifiers like OS, Python version, etc.
    ],
    license_files=["LICENSE"]
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
