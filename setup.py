from distutils.core import setup
setup(
    name='goldenrecords',
    version='1.0',
    packages=['goldenrecords'],
    licence='None',
    description='A simple API client for Golden Records',
    long_description=open('README.md').read(),
    install_requires=[
        'requests'
    ]
)