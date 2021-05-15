class Album:
    
    def __init__(self, id, title, genre, artist, price, year, songs):
        self.id = id
        self.title = title
        self.genre = genre
        self.artist_name = artist
        self.price = price
        self.release_year = year
        self.songs = songs


    def __str__(self):
        return str(self.id) + "|" +self.title + " | " + self.genre+ "|" + self.artist_name + "|"  + str(self.price) + "|" + str(self.release_year)