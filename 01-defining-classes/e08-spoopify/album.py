class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = [song for song in args]
        self.published = False

    def add_song(self, song):
        song_in_album = [s for s in self.songs if s == song]
        if self.published:
            return "Cannot add songs. Album is published."
        elif song_in_album:
            return f"Song is already in the album."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        song_to_remove = [s for s in self.songs if s.name == song_name]
        if self.published:
            return "Cannot remove songs. Album is published."
        elif not song_to_remove:
            return "Song is not in the album."
        song = song_to_remove[0]
        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = f"Album {self.name}\n"
        for song in self.songs:
            info += f"== {song.name} - {song.length}\n"
        return info

