class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        album_to_remove = [a for a in self.albums if a.name == album_name]
        if not album_to_remove:
            return f"Album {album_name} is not found."
        else:
            if album_to_remove[0].published:
                return "Album has been published. It cannot be removed."
        album = album_to_remove[0]
        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self):
        info = f"Band {self.name}\n"
        for album in self.albums:
            info += f"{album.details()}\n"
        return info
