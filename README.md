autopkglogparser
================

Parse an autopkg log and sends a mail if it encounters new items imported.


* Author: Kristian Botnen
* Email: kristian.botnen@adm.uib.no
* License: The MIT License


Installation:
```
$ git clone git@github.com:kbotnen/autopkglogparser.git
```
Usage:
```
$ python autopkglogparser.py -h
```
or
```
python autopkglogparser.py path/to/autopkg.log  to_address@domain.no from_address@domain.no smtp.domain.no
```
How I use it:

My autopkg setup consist of 4 parts.
* autopkglogparser.py
* autopkgrunner.sh
* recipes.txt
* tld.company.autopkglauncher.plist

Its applied in reverser order.

1: The LaunchDaemon fires of a the autopkgrunner.sh script every 7200 seconds.
2: The autopkgrunner.sh script reads the recipes.txt and does a autopkg run for each of the recipes listed.
3: The result of all the autopkg runs is piped to an output log.
4: When all the recipes in the recipes.txt are processed the bash scipt calls the autopkglogparser.py with needed arguments.
