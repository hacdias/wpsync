#!/usr/bin/python
#  _       ______  _____
# | |     / / __ \/ ___/__  ______  _____
# | | /| / / /_/ /\__ \/ / / / __ \/ ___/
# | |/ |/ / ____/___/ / /_/ / / / / /__
# |__/|__/_/    /____/\__, /_/ /_/\___/
#                    /____/
#
# Copyright (C) 2015 Henrique Dias <hacdias@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import subprocess
import shutil


class Svn:
    def __init__(self):
        self.commit = ''
        self.tag = ''

    def update(self):
        if self.tag is not '':
            repo = os.getcwd()
            trunk = os.path.join(repo, 'trunk')
            tags = os.path.join(repo, 'tags')
            new_tag = os.path.join(tags, self.tag)
            shutil.copytree(trunk, new_tag)

        if self.commit is '':
            print("You haven't mentioned the commit message.")
            exit(1)

        subprocess.call("svn add * --force", shell=True)
        subprocess.call("svn commit -m '" + self.commit + "'", shell=True)
