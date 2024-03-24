from setuptools import setup, find_packages

setup(
    name='bobtwine',
    version='0.4',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        # Your dependencies here
    ],
)
