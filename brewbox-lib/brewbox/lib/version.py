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

import os
import subprocess
import datetime
import logging

LOGGER = logging.getLogger(__name__)


def _get_git_changeset():
    """Returns a numeric identifier of the latest git changeset.

    The result is the UTC timestamp of the changeset in YYYYMMDDHHMMSS format.
    This value isn't guaranteed to be unique, but collisions are very unlikely,
    so it's sufficient for generating the development version numbers.
    """
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    git_log = subprocess.Popen('git log --pretty=format:%ct --quiet -1 HEAD',
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True, cwd=repo_dir, universal_newlines=False)
    (stdin, stderr) = git_log.communicate()
    try:
        timestamp = datetime.datetime.utcfromtimestamp(int(stdin))
    except ValueError:
        return None
    return timestamp.strftime('%Y%m%d%H%M%S')


def _get_version(version):
    "Returns a PEP 386-compliant version number from VERSION."

    # Bbuild the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    # | {a|b|c}N - for alpha, beta and rc releases

    parts = 2 if version[2] == 0 else 3
    main = '.'.join(str(x) for x in version[:parts])

    sub = ''
    if version[3] == 'alpha' and version[4] == 0:
        changeset = _get_git_changeset()
        if changeset:
            sub = '.dev%s' % changeset

    elif version[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        sub = mapping[version[3]] + str(version[4])

    return str(main + sub)


def get_pretty_version(v):
    return _get_version(v)
