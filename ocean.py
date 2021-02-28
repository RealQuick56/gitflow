import sys
import json

data_new = {'same': {}, 'different': {}}

for i in sys.stdin:
    k, v = i.rstrip('\n').split('** ')
    v = int(v)
    if v % 2 == 0 and len(str(v)) == 2 and '-' not in str(v):
        data_new['same'][k] = f'{v}'
    else:
        data_new['different'][k] = f'{v}'

with open('ocean.json', 'wt') as file:
    json.dump(data_new, file)

