import re

pattern = re.compile('[1][26][0][0]|[2][048][0][0]')
result = pattern.findall('2000')
if result == []:
    print("Bad")
else:
    print("OK ", result)