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

import unittest
from brewbox.utils import version


class VersionTestFunction(unittest.TestCase):

    def test_version_final(self):
        v = (0, 1, 0, 'final', 0)
        v_str = version.get_pretty_version(v)
        self.assertEqual('0.1', v_str)

    def test_version_alpha(self):
        v = (0, 1, 0, 'alpha', 1)
        v_str = version.get_pretty_version(v)
        self.assertEqual('0.1a1', v_str)
