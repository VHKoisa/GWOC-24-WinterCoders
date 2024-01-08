import requests

r = requests.post('localhost:3000/submit-form', params={'name':'vatsal'})
print(r)