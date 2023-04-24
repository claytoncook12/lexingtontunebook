import re
import typing as t
import datetime as datetime

tune_types: list[str] = [
    'reel','jig','hornpipe','slip jig','slide','mazurka'
]

class YoutubeVideoEmbed:
    """
    A class to represent a Embeded Youtube Video

    Attributes
    ----------
    title:
        The Video Title To Display
    instruments:
        Instruments playing tune in video
    embed url:
        Embed Youtube Url
    """

    def __init__(
        self,
        title: str,
        instruments: str,
        embed_url: str
    ):
        self.title = title
        self.instruments = instruments
        if is_valid_youtube_embed_url(embed_url):
            self.embed_url = embed_url
        else:
            raise ValueError(f'"{embed_url}" is not a valid embed youtube url')

class AudioReferences:
    """
    A class that represent a audio file

    Attributes
    ----------
    title
        The Audio Title
    instruments:
        Instruments playing tune in audio
    audio file name
        The name of the audio file that is located in static/audio
    """

    def __init__(
        self,
        title: str,
        instruments: str,
        audio_file_name: str,
    ):
        self.title = title
        self.instruments = instruments
        self.audio_file_name = audio_file_name

class Tune:
    """
    A class used to represent a Tune
    ...

    Attributes
    ----------
    title
        The Tune Title
    tune type
        The tune type
    ABC Notation
        The text for the abc notation
    Reference Videos
        A list of reference videos
    """    

    def __init__(
        self,
        title: str,
        tune_type: str,
        abc_notation: str,
        reference_videos: list[YoutubeVideoEmbed],
        reference_audios: list[AudioReferences]
    ):
        self.title = title
        if is_valid(tune_type, tune_types):
            self.tune_type = tune_type
        else:
            raise ValueError(f'"{tune_type}" is not a valid tune type.\n\tValid tune types are {tune_types}')
        self.abc_notation = abc_notation
        self.reference_videos = reference_videos
        self.reference_audios = reference_audios


def is_valid(input:str, valid_input: list[str]):
    return input in valid_input

def is_valid_youtube_embed_url(url:str) -> bool:
    if "https://www.youtube.com/embed/" in url:
        return True
    else:
        return False 