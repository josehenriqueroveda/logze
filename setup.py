from setuptools import setup, find_packages

setup(
    name='logze',
    version='0.1.2',
    description='Library in Python to store logs in MongoDB and send notifications of errors to Teams',
    author='Jose Henrique Roveda',
    author_email='josehenriqueroveda@usp.br',
    url='https://github.com/josehenriqueroveda/logze',
    packages=find_packages(),
    install_requires=[
        'pymongo',
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
