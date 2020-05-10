from setuptools import setup, find_packages

setup(
    name='pydensha',
    description='Japan Train Status Notifier',
    author='Gary Sentosa',
    author_email='gary.sentosa@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
