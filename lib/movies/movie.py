class Movie:
    def __init__(self, title, release_year, id = None):
        self.title = title
        self.release_year = release_year
        self.id = id

    def __eq__(self, other_movie):
        return self.__dict__ == other_movie.__dict__
    
    def __repr__(self):
        return f"Movie(id: {self.id}, title: {self.title}, release year: {self.release_year})"