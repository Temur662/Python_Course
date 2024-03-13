import requests
posts = {}
response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    print("Sucess!")
    posts = response.json()
    print(posts[0])
else:
    print("Error")

for post in posts[:5]:  # Limiting to first 5 posts for brevity
    print(f"Title: {post['title']}\nBody: {post['body']}\n")