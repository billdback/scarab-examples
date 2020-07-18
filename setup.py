"""
Copyright (C) 2020 William D. Back

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages

setup(name='scarab_examples',
      version='1.0',
      description='This package contains examples based on the Scarab framework.',
      python_requires='>3.7',
      author='William D Back',
      author_email='billback@mac.com',
      license='GPL3',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
            'scarab'
      ],
      dependency_links=[
            'http://github.com/billdback/scarab/tarball/master#egg=package-1.0'
      ]
      )
