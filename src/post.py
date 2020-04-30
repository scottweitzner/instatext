class Post:

    def __init__(self, image_url: str, caption: str, timestamp: int):
        self.image_url = image_url
        self.caption = caption
        self.date_posted = timestamp

    def __repr__(self):
        return f'Post[{self.image_url, self.caption}]'
