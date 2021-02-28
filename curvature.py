import json
import sys

data_new = {'unperturbed': {}, 'perturbed': {}}

for i in sys.stdin:
    k, v = i.rstrip('\n').split(': ')
    v = int(v)
    if v > 100 or v < -20:
        data_new['unperturbed'][k] = v
    else:
        data_new['perturbed'][k] = v

with open('curvature.json', 'wt') as file:
    json.dump(data_new, file)
