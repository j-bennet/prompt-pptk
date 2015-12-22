# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='prompt_pptk',
    description='CLI example with Python prompt toolkit',
    author='Iryna Cherniavska',
    url='http://github.com/j-bennet/prompt-pptk',
    download_url='http://github.com/j-bennet/prompt-pptk',
    author_email='i[dot]chernyavska[at]gmail[dot]com.',
    version='0.1',
    install_requires=[
        'prompt_toolkit>=0.46',
        'pygments>=2.0.2',
        'click>=4.1'
    ],
    extras_require={
        'testing': [
            'pytest>=2.7.0',
            'mock>=1.0.1',
            'tox>=1.9.2'
        ],
    },
    entry_points='''
        [console_scripts]
        pptk=prompt_pptk.main:main
    ''',
    packages=[],
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
