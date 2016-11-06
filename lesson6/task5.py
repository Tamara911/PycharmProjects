import re

patern2 = re.compile("[a-zA-Z][\w]*['@'][\w]+['.'][a-zA-Z]{2,3}")
result2 = patern2.findall("drg assd@dfgfg.com dfgfh dfhg@df.com fgnhf@fghf.ua")

for res in result2:
    print(res)