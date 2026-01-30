import re

lst = ['456rt6','86uet56','64yte789']

result = [''.join(re.findall(r'\d+', s)) for s in lst]
print(result)