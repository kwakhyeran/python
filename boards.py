import requests
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url).json()
for data in response:
    if data ['userId'] ==4:
        print(data['title'])
