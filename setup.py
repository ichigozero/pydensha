from setuptools import find_packages
from setuptools import setup

setup(
    name='pydensha',
    version='1.0.0',
    description='Japan Train Status Notifier',
    license='MIT',
    author='Gary Sentosa',
    author_email='gary.sentosa@gmail.com',
    url='https://github.com/ichigozero/pydensha',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    zip_safe=False,
    install_requires=[
        'gpiozero>=1.5.1',
    ],
)
