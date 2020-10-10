import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='sparksqlformatter',
    version='0.1.11',
    author='largecats',
    author_email='linfanxiaolinda@outlook.com',
    description=
    'A SparkSQL formatter in Python based on https://github.com/zeroturnaround/sql-formatter, with customizations and extra features.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/largecats/sparksql-formatter',
    packages=setuptools.find_packages(),
    install_requires=['configparser'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': ['sparksqlformatter=sparksqlformatter:run_main'],
    })
