class message:
    def __init__(self, body='', file='', embed=None, author=None, server=None):
        self.command = None
        self.author = None
        self.server = None
        self.body = body
        self.file = file
        self.embed = embed
