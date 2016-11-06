# 1. html file, find name of tags, get list of tags
# example:  - need to get name only
# <name> aaa </name>

# 2. email aa.bb.cdf@gmail.com

# {2,3} - remove

# 3. Give a year, find if year divide on 4 and not divide on 100 - use only regular expression

import re

pattern = '[\/](\w+)[\>]'
string = '<b> text</b> \
<p> dfgfgd </p> \
<aaa> dghdg </aaa>'
a = re.findall(pattern,string)
print(a)
