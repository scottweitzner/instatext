import json
from typing import List, Union

import requests
from bs4 import BeautifulSoup

from src.post import Post


def get_latest_n_posts_for_profile(profile: str, n: int = 5) -> List[Post]:
    insta_link = f'https://www.instagram.com/{profile}'

    posts = []
    soup = BeautifulSoup(requests.get(insta_link).content, features='html.parser')
    script = soup.find('script', text=lambda text: text.startswith('window._sharedData'))
    json_string = script.text.split(' = ')[1].rstrip(';')
    json_data = json.loads(json_string)

    profile_object = json_data['entry_data']['ProfilePage'][0]
    for idx, post in enumerate(profile_object['graphql']['user']['edge_owner_to_timeline_media']['edges']):
        if idx > n:
            break
        post_link = post['node']['display_url']
        post_caption = post['node']['edge_media_to_caption']['edges'][0]['node']['text']
        post_timestamp = post['node']['taken_at_timestamp']
        posts.append(Post(post_link, post_caption, post_timestamp))

    return posts


def get_latest_post_for_profile(profile: str) -> Union[Post, None]:
    post = get_latest_n_posts_for_profile(profile, 1)
    if len(post) < 1:
        return None
    return post[0]
