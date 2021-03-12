import requests
url = input("Input the URL:\n")

r = requests.get(url)

if r.status_code == 200:
    r_json = (r.json())
    if 'content' in r_json:
        print(r_json.get('content'))
    else:
        print("Invalid quote resource!")
else:
    print("Invalid quote resource!")
