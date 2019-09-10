#!/usr/bin/env python

from distutils.core import setup

setup(
    name='LogoExportSM',
    version='0.1.01',
    scripts=['logoexportsm'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    author='Sebastian Weiss <agentur@3ele.de>',
    author_email='<agentur@3ele.de>',
    url='https://github.com/3ele-projects/auto_export_svg/',
    install_requires=['svgwrite', 'lxml', 'pycairo', 'svgutils'],
)