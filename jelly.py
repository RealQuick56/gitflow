import argparse
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-digit', type=str)
parser.add_argument('post', type=str)
parser.add_argument('key', type=str)
parser.add_argument('--negative', default=-1, type=int)
parser.add_argument('--largest', default=100, type=int)
args = parser.parse_args()
print(args)
url = f'http://{args.host}:{args.port}'
#response = requests.get(url)
#response = response.json()
response = """{
    "chemical": {
        "fission": [
            98,
            -9,
            12,
            93,
            112
        ],
        "synthesis": [
            11,
            63,
            95
        ],
        "transformation": [
            -3,
            59,
            37,
            64,
            11
        ]
    },
    "nuclear": {
        "fission": [
            54,
            56,
            54,
            115,
            39
        ],
        "synthesis": [
            9,
            -3,
            54,
            97
        ],
        "transformation": [
            110,
            38,
            54
        ]
    }
}"""
data = json.loads(response)[args.key]
for k, v in data.items():
    ans.append(f"{k}#{sum(v)}#{min(v)}#")
    print(k, v)
ans.sort()