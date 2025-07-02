import requests

class Post:

    def fetch_post(self):
        return requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
