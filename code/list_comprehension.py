lst = ['456rt6','86uet56','64yte789']

res = [''.join(ch for ch in s if ch.isdigit()) for s in lst]

print(res)