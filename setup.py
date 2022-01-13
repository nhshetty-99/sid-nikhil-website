"""
Insta485 python package configuration.

Christopher Huggins <huggscbm@umich.edu>
Sidharth Reddy <sidkr@umich.edu>
Nikhil Shetty <nhshetty@umich.edu>
"""

from setuptools import setup

setup(
    name='michigan',
    version='0.1.0',
    packages=['michigan'],
    include_package_data=True,
    install_requires=[
        'arrow==0.15.5',
        'bs4==0.0.1',
        'Flask==1.1.1',
        'html5validator==0.3.3',
        'pycodestyle==2.5.0',
        'pydocstyle==5.0.2',
        'pylint==2.4.4',
        'pytest==5.3.4',
        'requests==2.22.0',
        'sh==1.12.14',
    ],
)
