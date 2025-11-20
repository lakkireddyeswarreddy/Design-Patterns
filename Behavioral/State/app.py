
from media_player import MediaPlayer
from playing_state import PlayingState

if __name__ == "__main__":
    
    media_player = MediaPlayer()
    media_player.set_current_state(PlayingState("Chikiri Chikiri"))
    media_player.play()
    media_player.pause()
    media_player.resume()
    media_player.stop()

    