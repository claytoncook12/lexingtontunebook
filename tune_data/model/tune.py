import re
import typing as t
import datetime as datetime

tune_types: list[str] = [
    'reel','jig','hornpipe','slip jig'
]

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
        reference_videos: list[str]
    ):
        self.title = title
        if is_valid(tune_type, tune_types):
            self.tune_type = tune_type
        else:
            raise ValueError(f'"{tune_type}" is not a valid tune type.\n\tValid tune types are {tune_types}')
        self.abc_notation = abc_notation
        self.reference_videos = reference_videos

def is_valid(input:str, valid_input: list[str]):
    return input in valid_input