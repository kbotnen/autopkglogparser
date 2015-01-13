#!/bin/bash
/usr/local/munki/makecatalogs /Data/Munki/repo/
/usr/local/bin/autopkg repo-update all
> /tmp/tld.company.autopkglauncher_out.log
while read line
do
    /usr/local/bin/autopkg run -v $line
done < /Users/munki/recipes.txt
/usr/local/munki/makecatalogs /Data/Munki/repo/
/usr/bin/python /Users/munki/autopkglogparser.py /tmp/tld.company.autopkglauncher_out.log receivere@example.com sender@example.com smtp.company.tld
