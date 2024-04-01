class Category: 
    def __init__(self, name, words_and, like_and, words_or, like_or, filters):
        self.name = name
        self.words_and = words_and
        self.like_and = like_and
        self.words_or = words_or
        self.like_or = like_or
        self.filters = filters