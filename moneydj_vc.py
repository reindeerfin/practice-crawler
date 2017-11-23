import requests, json
url = 'https://www.moneydj.com/InfoSvc/apis/vc'
payload = {
    "counts" : [{"svc":"NV","guid":"d179e264-0181-47c5-a86b-0dc72919990d"}]
}
head = { "Content-Type" : "application/json" }
res = requests.post(url, data = json.dumps(payload), headers = head)
print(res)
print(res.text)
