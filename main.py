import requests

headers = {
    'User-Agent': '',
    'Referer': '',
}

url = ''  

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()  
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
