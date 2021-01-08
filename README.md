# PyMusicPlayer
![Downloads](https://img.shields.io/pypi/dm/pymusicplayer?style=flat-square)
![License](https://img.shields.io/pypi/l/pymusicplayer?style=flat-square)
![Version](https://img.shields.io/pypi/v/pymusicplayer?label=version&style=flat-square)
![Format](https://img.shields.io/pypi/format/pymusicplayer?style=flat-square)
![Last Update](https://img.shields.io/github/last-commit/cmdvmd/pymusicplayer?style=flat-square)

An MP3 music player interface for Python with builtin playback and queue functionality built using [Pygame mixer](https://www.pygame.org/docs/ref/music.html)

### Installation
Install via `pip`

```
$ pip install pymusicplayer
```

## Usage

```python
from pymusicplayer import MusicPlayer

mp = MusicPlayer()
```

* `add_song(filename, song_name)` - Add song to queue by filename and sets song name (defaults to filename) 
* `remove_song(index)` - Remove song at index of queue
* `get_current_song()` - Return name of currently loaded song
* `get_queue()` - Return names of songs in queue
* `get_loop_queue()` - Return if queue will loop
* `set_loop_queue()` - Set if queue should loop
* `shuffle()` - Shuffle songs in queue
* `is_playing()` - Return if music is currently playing
* `play()` - Start playing loaded music
* `pause()` - Pause loaded music
* `restart()` - Restart loaded music
* `get_volume()` - Returns volume of music
* `set_volume(volume)` - Sets volume of music to value in interval [0, 100]
* `get_pos()` - Get current position of loaded music in milliseconds
* `set_pos(pos)` - Set position of loaded music in milliseconds
* `choose_song(index)` - Load song at index in queue
* `next_song()` - Load next song in queue
* `previous_song()` - Load previous song in queue
* `skip(amount)` - Skip amount (in milliseconds) in music (positive for forward, negative for rewind)