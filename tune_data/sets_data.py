from tune_data.model.sets import Set
from tune_data.tune_data import tune_dict

set_list: list[Set] = [
    Set(
        'reel',
        [tune_dict["Cooley's"], tune_dict["The Wise Maid"]]
    )
]