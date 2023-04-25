from tune_data.model.tune import Tune, tune_types, is_valid

set_types: list[str] = tune_types

class Set:
    """
    A class representing a set of tunes

    Attributes
    ----------
    Set List
        The tunes in the set
    """

    def __init__(
        self,
        set_type: str,
        set_list: list[Tune]
    ):
        if is_valid(set_type, set_types):
            self.set_type = set_type
        else:
            raise ValueError(f'"{set_type}" is not a valid set type.\n\tValid set types are {set_types}')
        self.set_list = set_list

    def set_name(self) -> str:
        set_name_str = ''
        for tune in self.set_list:
            if tune == self.set_list[-1]:
                set_name_str += tune.title
            else:
                set_name_str += tune.title + " - "
        
        return set_name_str