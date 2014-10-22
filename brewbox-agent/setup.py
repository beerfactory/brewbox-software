# Copyright (C) 2014  Nicolas Jouanin and others
#
# This file is part of brewbox.
#
# Brewbox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Brewbox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Brewbox.  If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup, find_packages
from pybone import version_info

setup(
    name="brewbox-agent",
    version=version_info,
    description="Brewbox agent package for managing brewbox hardware I/O board",
    url="https://github.com/beerfactory/brewbox-agent",
    license='GPLv3',
    packages=find_packages(exclude=['tests']),
    classifiers=[
    ],
    requires=[]
)