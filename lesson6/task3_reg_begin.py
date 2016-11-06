# [a] - start and finish a - one letter
# [ab] - start or end "a" or "b"
# [a-z] - one any letter
# [a-c,z] - from a to c and z
# [a-cA-Z]
# [a-zA-Z0-9] = \w
# [0-9] = \d
# [^] - NOT
# [^a-zA-Z0-9] = \W
# [^0-9] = \D - NOT DIGIT
# \s - ""
# \S - not probel
# [a]+ = a, aa, aaa, ... = a+
# [a]* - 0 or more
# [a]? - 0 or 1 symbol
# [a]{3-5} - aaa, aaaa, aaaaa
# [a]{3,} - 3 or more
# [a]{,5} - till 5 included
# [a]+[y] = aaaa...aay (any a and finish y)
# [a][\w]+[y] = a(one or more letter)y
# () - group
# [a]([\w]+)[y]
# abbcdfy = all -zero group, bbcdf - first
# ([\w]+)([\w]*) - first max, second - min
# $ - end of line
# . - any symbol

import re

pattern = '(210)'
string = '210 fghfc gtr 322 21'
a = re.findall(pattern,string)
print(a)