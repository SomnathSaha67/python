class Playlist:

  def __init__(self, name, songs):
    self.name= name
    self.songs= songs

  def __eq__(self, other):
    if isinstance(other, Playlist):
      return self.songs==other.songs
    return False
  
  def __len__(self):
    return len(self.songs)

p1 = Playlist("Morning Vibes", ["SongA", "SongB", "SongC"])
p2 = Playlist("Workout Mix", ["SongA", "SongB", "SongC"])
p3 = Playlist("Chill", ["SongX", "SongY"])

print(p1==p2)
print(p1==p3)

print(len(p1))
print(len(p3))