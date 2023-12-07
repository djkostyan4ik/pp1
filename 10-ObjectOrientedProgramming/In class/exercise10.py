class Music():
    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year

    def __str__(self):
        return 'Performer: ' + self.artist +'\n' + "Song: " + self.track_title + '\n' + 'Album: ' + self.album + '\n' + 'Year: ' + self.year 
    
my_music = Music('Ed Sheeran',"Hearts Don't Break Around Here",'Divide', '2017')
print(my_music)
my_music2 = Music('Scorpions','Wind of Change','Crazy world', '1990')
print(my_music2)