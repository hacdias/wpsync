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

from .composer import Composer
from .bower import Bower
from .plugin import Plugin


def main():
    config_file = 'wpsync.json'

    if not os.path.isfile(config_file):
        print('There is no configuration file.')
        exit(1)

    config = json.loads(open(config_file).read())

    if 'plugin' not in config:
        print('You have problems in the configuration file.')
        exit(1)

    if 'wordpress-svn' not in config:
        print("You haven't defined the WordPress SVN link.")
        exit(1)

    if 'trunk' in config['wordpress-svn']:
        print('Please remove "trunk" from the SVN link.')
        exit(1)

    if os.path.isfile('composer.json'):
        composer = Composer()
        composer.update()

    if os.path.isfile('bower.json'):
        bower = Bower()
        bower.update()

    plugin = Plugin()
    plugin.plugin_file = config['plugin']['main'] if 'main' in config['plugin'] else 'plugin.php'
    plugin.index = config['increase'] if 'increase' in config else 'build'

    if os.path.isdir('.svn'):
        plugin.version_control = 'svn'

    plugin.wordpress_svn = config['wordpress-svn']

    if 'ignore' in config:
        plugin.ignore_files = config['ignore']

    plugin.update()

    try:
        input("Press any key to continue...")
    except SyntaxError:
        pass
