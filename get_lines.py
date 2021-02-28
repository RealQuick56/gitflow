import requests
import sys
server = input()
port = input()
a = input()
b = input()

params = {'a': a, 'b': b}
response = requests.get(f'{server}:{port}', params=params).json()

numbers = [int(x) for x in response['result']]
numbers.sort()
print(numbers[0], numbers[1])
print(response['check'])