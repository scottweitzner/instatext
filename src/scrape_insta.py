import json
from typing import List

import requests
from bs4 import BeautifulSoup

from post import Post


def scrape_insta(username: str) -> List[Post]:
    insta_link = f'https://www.instagram.com/{username}'

    posts = []
    soup = BeautifulSoup(requests.get(insta_link).content, features='html.parser')
    script = soup.find('script', text=lambda text: text.startswith('window._sharedData'))
    json_string = script.text.split(' = ')[1].rstrip(';')
    json_data = json.loads(json_string)

    profile_object = json_data['entry_data']['ProfilePage'][0]
    for post in profile_object['graphql']['user']['edge_owner_to_timeline_media']['edges']:

        post_link = post['node']['display_url']
        post_caption = post['node']['edge_media_to_caption']['edges'][0]['node']['text']
        posts.append(Post(post_link, post_caption))

    return posts
