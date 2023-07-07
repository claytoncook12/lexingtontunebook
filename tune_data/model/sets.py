from tune_data.model.tune import Tune, AudioReferences, tune_types, is_valid
from shared_functions import slugify

set_types: list[str] = tune_types

class Set:
    """
    A class representing a set of tunes

    Attributes
    ----------
    Set Tune List
        The tunes in the set
    """

    def __init__(
        self,
        set_type: str,
        set_tune_list: list[Tune],
        reference_audios: list[AudioReferences]
    ):
        if is_valid(set_type, set_types):
            self.set_type = set_type
        else:
            raise ValueError(f'"{set_type}" is not a valid set type.\n\tValid set types are {set_types}')
        self.set_tune_list = set_tune_list
        self.reference_audios = reference_audios

    def set_name(self) -> str:
        set_name_str = ''
        for tune in self.set_tune_list:
            if tune == self.set_tune_list[-1]:
                set_name_str += tune.title_and_key()
            else:
                set_name_str += tune.title_and_key() + " - "
        
        return set_name_str
    
    def slug_id(self) -> str:
        return slugify(self.set_name())