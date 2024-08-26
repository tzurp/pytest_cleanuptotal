from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pytest-cleanuptotal',
    packages=['pytest_cleanuptotal'],
    package_dir={'pytest_cleanuptotal': 'src/pytest_cleanuptotal'},
    version='0.2.2',
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
