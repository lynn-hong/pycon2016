__author__ = 'Lynn'
__email__ = 'lynnn.hong@gmail.com'
__date__ = '8/15/2016'


from setuptools import setup, find_packages

setup(
    name='template_korean',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'django',
        'korean',
    ]
)