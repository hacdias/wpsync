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
import json
import subprocess
import shutil


class Bower:
    def __init__(self):
        self.main = 'bower.json'
        self.cnf = '.bowerrc'
        self.json = json.loads(open(self.main).read())
        self.folder = 'bower_components'
        self.config = ''
        self.__check_folder()

    def __check_folder(self):
        if os.path.isfile(self.cnf):
            self.config = json.loads(open(self.cnf).read())

            if 'directory' in self.config:
                self.folder = self.config['directory']

        self.folder = os.path.normpath(self.folder)

    def update(self):
        if os.path.isdir(self.folder):
            shutil.rmtree(self.folder)

        subprocess.call('bower install', shell=True)
