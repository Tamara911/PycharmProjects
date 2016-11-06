import re

patern2 = re.compile("[a-zA-Z][\w]*['@']([\w]+['.'])+[a-zA-Z]{2,3}")
result2 = patern2.finditer("drg assd@dfgfg.dfgh.dfhgd.com dfgfh dfhg@df.com fgnhf@fghf.com.ua")

for res in result2:
    print(res.group(0))