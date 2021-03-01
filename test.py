import requests
url = "http://sntc.iitmandi.ac.in:3000/submissions/?base64_encoded=false&wait=true"
headers = {
    "cache-control": "no-cache",
    "Content-Type": "application/json"
}
# body = {
#     "source_code": "print('hello world')",
#     "language_id": 34,
#     "stdin": "",
#     "cpu_time_limit": 5
# }
body = {}
body["source_code"] = "print('hello world')"
body["language_id"] = 34
body["stdin"] = ""
body["cpu_time_limit"] = 5
print(body)
response = requests.post(url, headers=headers, data=body)
print(response.content)
