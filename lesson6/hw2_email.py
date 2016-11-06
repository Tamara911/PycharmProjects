# 2. email aa.bb.cdf@gmail.com

import re

patern2 = re.compile("([\w]+['.'])+[a-zA-Z][\w]*['@']([\w]+['.'])+[a-zA-Z]{2,3}")
result2 = patern2.finditer("drg tamara.grytyk@gmail.com dfgfh dfhg@df.com fgnhf@fghf.com.ua")

for res in result2:
    print(res.group(0))
