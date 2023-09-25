from setuptools import find_packages, setup

setup(
    name='pytest-cleanuptotal',
    packages=['pytest_cleanuptotal'],
    package_dir={'pytest_cleanuptotal': 'src/pytest_cleanuptotal'},
    version='0.2',
    author='Tzur Paldi',
    author_email='tzur.paldi@outlook.com',
    maintainer='Tzur Paldi',
    maintainer_email='tzur.paldi@outlook.com',
    license='GNU',
    url='',
    description='A cleanup plugin for pytest',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
    ],
    entry_points={
        'pytest11': [
            'pytest_cleanuptotal = pytest_cleanuptotal.cleanuptotal',
        ],
    },
)
