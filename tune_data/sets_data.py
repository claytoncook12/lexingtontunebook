from tune_data.model.sets import Set
from tune_data.model.tune import AudioReferences
from tune_data.tune_data import tune_dict

set_list: list[Set] = [
    # REELS
    Set(
        'reel',
        [tune_dict["Cooley's"], tune_dict["Wise Maid, The"]],
        [AudioReferences(
            "Cooley's - Wise Maid (unaccompanied)","flute","Cooley's - Wise Maid - flute- 80 bpm.mp3"
        )]
    ),
    Set(
        'reel',
        [tune_dict["Concertina Reel"], tune_dict["Ships are Sailing"], tune_dict["Father Kelly's"]],
        [AudioReferences(
            "The Concertina - Ships Are Sailing- Father Kelly's (unaccompanied)",
            "fiddle",
            "05 The Concertina_Ships Are Sailing_Father Kelly's (unaccompanied).mp3")
        ]
    )
    ,
    # JIGS
    Set(
        'jig',
        [tune_dict["Kesh"], tune_dict["Morrison's"], tune_dict["Tripping Up the Stairs"]],
        [AudioReferences("Kesh - Morrison's - Tripping Up the Stairs (unaccompanied)","flute", "Kesh - Morrsion - Tripping - flute - 100 bpm.mp3")]
    ),
    Set(
        'jig',
        [tune_dict["Connaughtman's Rambles"], tune_dict["Pipe On The Hob"]],
        [AudioReferences("Connaughtman's Rambles - Pipe On the Hob (unaccompanied)", "flute","Conn - Pipe On the Hob - flute - 100 bpm.mp3")]
    ),
    # SLIP JIGS
    Set(
        'slip jig',
        [tune_dict["Little Fair Canavans"], tune_dict["Redican's Mother"], tune_dict["Humours of Derrycrossane"]],
        []
    ),
    # POLKAS
    Set(
        'polka',
        [tune_dict["I Looked East And I Looked West"],tune_dict["Julia Clifford's"],tune_dict["Scartaglen"]],
        [AudioReferences(
            "Julia Clifford's - I Looked East And I Looked West - Scartaglen (unaccompanied)",
            "fiddle",
            "Julia Clifford's - I Looked East And I Looked West - Scartaglen (unaccompanied).mp3")]
    ),
    Set(
        'slide',
        [tune_dict["Where's the Cat"], tune_dict["The Cat's Rambles to the Child's Saucepan"]],
        [AudioReferences("Cat Slides","flute","2023-10-03 Wheres the Cat - Cats Rambles to the Child's Saucepan slides.mp3")]
    ),
    # Hornpipe
    Set(
        'hornpipe',
        [tune_dict["Humours of Tuamgraney"],tune_dict["Walsh's"]],
        [AudioReferences("Humors of Tuamgraney - Walsh's","fiddle","2023-07-30 Humors of Tuamgraney - Walsh's.mp3")]
    ),
    # MAZURKA
    # WALTZES
    # MARCHES
    # Hop Jigs
    # Set Dance
    Set(
        'set dance',
        [tune_dict["Three Sea Captians"]],
        [AudioReferences("Three Sea Captains","mandolin","2023-07-30 Three Sea Captains.mp3")]
    )
]