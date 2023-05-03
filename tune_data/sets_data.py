from tune_data.model.sets import Set
from tune_data.model.tune import AudioReferences
from tune_data.tune_data import tune_dict

set_list: list[Set] = [
    # REELS
    Set(
        'reel',
        [tune_dict["Cooley's"], tune_dict["Wise Maid, The"]],
        [AudioReferences(
            "Cooley's - Wise Maid (unaccompanied)","flute (Clayton Cook)","Cooley's - Wise Maid - flute- 80 bpm.mp3"
        )]
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
    Set(
        'jig',
        [tune_dict["Kesh"], tune_dict["Morrison's"], tune_dict["Tripping Up the Stairs"]],
        [AudioReferences("Kesh - Morrison's - Tripping Up the Stairs (unaccompanied)","flute (Clayton Cook)", "Kesh - Morrsion - Tripping - flute - 100 bpm.mp3")]
    ),
    Set(
        'jig',
        [tune_dict["Larry O'Gaff's"], tune_dict["Geese in the Bog"], tune_dict["Jimmy Ward's"]],
        []
    ),
    Set(
        'jig',
        [tune_dict["Connaughtman's Rambles"], tune_dict["Pipe On The Hob"]],
        [AudioReferences("Connaughtman's Rambles - Pipe On the Hob (unaccompanied)", "flute (Clayton Cook)","Conn - Pipe On the Hob - flute - 100 bpm.mp3")]
    ),
    # SLIP JIGS
    Set(
        'slip jig',
        [tune_dict["A Fig For A Kiss"], tune_dict["O'Farrell's Welcome to Limerick"]],
        []
    ),
    Set(
        'slip jig',
        [tune_dict["Barony Jig, The"], tune_dict["Snowy Path, The"]],
        []
    ),
    Set(
        'slip jig',
        [tune_dict["Little Fair Canavans"], tune_dict["Redigan's Mother"], tune_dict["Humours of Derrycrossane"]],
        []
    ),
    # POLKAS
    Set(
        'polka',
        [tune_dict["I Looked East And I Looked West"],tune_dict["Julia Clifford's"],tune_dict["Scartaglen"]],
        [AudioReferences(
            "Julia Clifford's - I Looked East And I Looked West - Scartaglen (unaccompanied)",
            "fiddle (Justin Bonar-Bridges)",
            "Julia Clifford's - I Looked East And I Looked West - Scartaglen (unaccompanied).mp3")]
    ),
    # SLIDES
    Set(
        'slide',
        [tune_dict["Denis Murphy's"], tune_dict["O'Keefe's"], tune_dict["Going to the Well For Water"]],
        []
    ),
    Set(
        'slide',
        [tune_dict["Mom's Favorite"], tune_dict["Brosna, The"]],
        []
    ),
    Set(
        'slide',
        [tune_dict['Scattery Island'], tune_dict["Jack Regan's"]],
        []
    ),
    # MAZURKA
    Set(
        'mazurka',
        [tune_dict["Shoe The Donkey"]],
        []
    )
]