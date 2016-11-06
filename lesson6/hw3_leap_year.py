# 3. Give a year, find if year divide on 4 and not divide on 100 - use only regular expression

import re

pattern = re.compile('(^\d{0,2}[13579][26]|^\d{2}[2468][048]|^\d{2}[0][48])|([13579][26][0][0]|[2468][048][0][0])')
result = pattern.findall('32')
if result == []:
    print("Bad")
else:
    print("OK ", result)

