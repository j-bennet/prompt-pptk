# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='prompt_pptk',
    description='CLI example with Python prompt toolkit',
    author='Iryna Cherniavska',
    url='http://github.com/j-bennet/prompt-pptk',
    download_url='http://github.com/j-bennet/prompt-pptk',
    author_email='i[dot]chernyavska[at]gmail[dot]com.',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'prompt_toolkit>=0.46',
        'pygments>=2.0.2',
        'click>=4.1'
    ],
    entry_points='''
        [console_scripts]
        pptk=prompt_pptk.main:main
    ''',
    scripts=[],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
