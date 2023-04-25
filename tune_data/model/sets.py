from tune_data.model.tune import Tune

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
        set_list: list[Tune]
    ):
        self.set_list = set_list

    def set_name(self) -> str:
        set_name_str = ''
        for tune in self.set_list:
            if tune == self.set_list[-1]:
                set_name_str += tune.title
            else:
                set_name_str += tune.title + " - "
        
        return set_name_str