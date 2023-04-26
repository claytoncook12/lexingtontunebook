from tune_data.model.sets import Set
from tune_data.model.tune import AudioReferences
from tune_data.tune_data import tune_dict

set_list: list[Set] = [
    # REELS
    Set(
        'reel',
        [tune_dict["Cooley's"], tune_dict["Wise Maid, The"]],
        []
    ),
    Set(
        'reel',
        [tune_dict["Concertina Reel"], tune_dict["Ships are Sailing"], tune_dict["Father Kelly's"]],
        [AudioReferences(
            "The Concertina - Ships Are Sailing- Father Kelly's (unaccompanied)",
            "fiddle (Justin Bonar-Bridges)",
            "05 The Concertina_Ships Are Sailing_Father Kelly's (unaccompanied).mp3")
        ]
    )
    ,
    Set(
        'reel',
        [tune_dict["Sally Gardens"], tune_dict['Merry Blacksmith']],
        []
    ),
    # JIGS
    Set(
        'jig',
        [tune_dict["Lanigan's Ball"], tune_dict["Whistling Postman, The"], tune_dict["Out On The Ocean"]],
        []
    ),
    # SLIP JIGS
    Set(
        'slip jig',
        [tune_dict["A Fig For A Kiss"], tune_dict["O'Farrell's Welcome to Limerick"]],
        []
    ),
    # POLKAS
    Set(
        'polka',
        [tune_dict["I Looked East And I Looked West"],tune_dict["Julia Clifford's"],tune_dict["Scartaglen"]],
        []
    ),
    # SLIDES
    Set(
        'slide',
        [tune_dict["Mom's Favorite"], tune_dict["Brosna, The"]],
        []
    ),
    # MAZURKA
    Set(
        'mazurka',
        [tune_dict["Shoe The Donkey"]],
        []
    )
]