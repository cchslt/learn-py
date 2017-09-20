from collections import defaultdict

d = defaultdict(lambda : '不存在')
d['key1'] = 'ffg'
print(d['key1'])
print(d['key2'])

