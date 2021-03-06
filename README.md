# WPSync

[![Build](https://img.shields.io/travis/hacdias/wpsync.svg?style=flat-square)](https://travis-ci.org/hacdias/wpsync)
[![Latest Stable Release](https://img.shields.io/github/release/hacdias/wpsync.svg?style=flat-square)](https://github.com/hacdias/wpsync/releases)
[![License](https://img.shields.io/github/license/hacdias/wpsync.svg?style=flat-square)](https://github.com/hacdias/wpsync/blob/master/LICENSE)

Do you use a GitHub, or any other git or svn repository, for the development of your WordPress plugin? Are you bored of copying and pasting all of the files when you launch a new version of your plugin? Are you bored of changing the plugin version every time? This is the perfect solution for you!

### Menu

- [Features](#features)
- [Installation](#installation)
  + [Linux and OS X](#linux-and-os-x)
  + [Windows](#windows)

## Features

* Updates [bower](https://github.com/bower/bower) and [composer](https://github.com/composer/composer) dependencies;
* Edits the files and sets the new version of the plugin;
* Updates both DEV and WP SVN repositories, creating a tag;
* Ignores the folders/files you want;
* Synchronize main repository's "\_assets" folder with WordPress SVN "assets".

## Installation

Go to [downloads page](https://github.com/hacdias/wpsync/releases) and download the package for your operating system and architecture. Then, unzip the files, and put the executable somewhere covered by PATH variable.

### Linux and OS X

Just run the following commands, replacing ```$VERSION``` by the current version, ```$OS``` by your operating system name and ```$ARCH``` by your operating system's architecture.

```bash
curl -LOk https://github.com/hacdias/wpsync/releases/download/$VERSION/$OS_$ARCH.zip
unzip wpsync_$OS_$ARCH.zip
sudo cp wpsync /usr/local/bin
```

### Windows

Unzip the downloaded folder and run ```install.bat``` as admin.

## Usage

You should run the command ```wpsync init --link="WORDPRESS_SVN_URL"``` in the root of your project. It creates a ```wpsync.json``` file. Should have a content like this:

```json
{
  "increase": "build",
  "plugin": {
    "main": "plugin.php",
    "svn": "https://plugins.svn.wordpress.org/hackerrank-profile-widget/",
  },
  "dependencies": {
    "bower": true,
    "composer": true
  },
  "ignore": [
    ".idea"
  ]
}

```

* ```increase``` is the default version increase (nomenclature: ```major.minor[.build[.revision]]```);

* ```main``` refers to plugin's main file;

* ```svn``` is the link for the WordPress SVN;

* ```ignore``` is an array of files/folders you don't want to upload to the WordPress SVN.

After having a ```.wpsync``` file on the root of your project, you just have to run the following command from console:

```
wpsync [commands] [options]
```

Run ```wpsync -h``` to know more.
