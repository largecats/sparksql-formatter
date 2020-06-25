import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='hiveql-formatter-largecats', # Replace with your own username
    version='0.0.1',
    author='largecats',
    author_email='linfanxiaolinda@outlook.com',
    description='A HiveQL formatter in Python based on [sql-formatter](https://github.com/zeroturnaround/sql-formatter) and its fork [sql-formatter-plus](https://github.com/kufii/sql-formatter-plus), with customizations and extra features.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/largecats/hiveql-formatter',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': ['hiveql-formatter = hiveql-formatter:main'],
    },
)