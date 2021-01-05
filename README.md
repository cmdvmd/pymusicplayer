# PYMP
An mp3 music player interface for Python

### Installation
Install via `pip`

```
$ pip install pymp
```

## Usage
```python
from pymp import MusicPlayer

mp = MusicPlayer()
```

### The Song Class
The format the `MusicPlayer` class stores songs
* `length` - Length of song in milliseconds
* `prepare()` - Unload previous song & prepare this song to be played

### Methods
* `add_song(file_name)` - Add song to queue by file name
* `add_song(file)` - Add song to queue by `BytesIO` stream
* `add_song(song)` - Add song to queue by [`Song`](#the-song-class)
* `get_current_song()` - Return [`Song`](#the-song-class) object of loaded song
* `is_playing()` - Return if music is currently playing
* `play()` - Start playing loaded music
* `pause()` - Pause loaded music
* `get_pos()` - Get current position of loaded music in milliseconds
* `set_pos(pos)` - Set position of loaded music in milliseconds
* `choose_song(index)` - Load song at index in queue
* `next_song()` - Load next song in queue
* `previous_song()` - Load previous song in queue
* `skip(amount)` - Skip amount (in milliseconds) in music (positive number for forward, negative number for rewind)
* `restart()` - Restart loaded music
