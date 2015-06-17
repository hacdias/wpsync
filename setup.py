from setuptools import setup

setup(
    name='wpsync',
    version='1.0.1',
    packages=['wpsync'],
    url='https://github.com/refactors/wpsync',
    author='Henrique',
    author_email='hacdias@gmail.com',
    description='A tool to sync the WordPress SVN with your Git (or SVN) repository.',
    license='GNU General Public License v3 or later (GPLv3+)',
    keywords=["wordpress", "svn", "git", "sync"],
    platforms='any',
    entry_points={
        'console_scripts': [
            'wpsync = wpsync.wpsync:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Natural Language :: English",
        "Topic :: Software Development :: Version Control",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities"
    ],
)
