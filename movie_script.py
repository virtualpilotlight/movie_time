import requests

url = input("What's the link??? ")
# what_is_it = input("file type?")

query_apameters = {"downloadformat": "mp4"}

response = requests.get(url, params=query_apameters)
# print(link_name)
# response.url
# response.ok
# response.status_code

with open("movie.mp4", mode="wb") as file:
     file.write(response.content)

# https://archive.org/download/youtube-DAi1ahospLI/DAi1ahospLI.mp4
