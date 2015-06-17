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


class Composer:
    def __init__(self):
        self.main = 'composer.json'
        self.lock = 'composer.lock'
        self.json = json.loads(open(self.main).read())
        self.folder = 'vendor'
        self.__check_folder()

    def __check_folder(self):
        if 'config' in self.json:
            if 'vendor-dir' in self.json['config']:
                self.folder = self.json['config']['vendor-dir']

        self.folder = os.path.normpath(self.folder)

    def update(self):
        if os.path.isfile(self.lock):
            os.remove(self.lock)

        if os.path.isdir(self.folder):
            shutil.rmtree(self.folder)

        subprocess.call('composer install', shell=True)
