class Post:

    def __init__(self, image_url: str, caption: str):
        self.image_url = image_url
        self.caption = caption

    def __repr__(self):
        return f'Post[{self.image_url, self.caption}]'
