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
    Set(
        'reel',
        [tune_dict["Miss McLeod's"], tune_dict['Merry Blacksmith'], tune_dict["Sally Gardens"]],
        []
    ),
    Set(
        'reel',
        [tune_dict["Devanney's Goat"], tune_dict["Geenfields of Rossbeigh"], tune_dict['Maid Behind the Bar, The']],
        []
    ),
    Set(
        'reel',
        [tune_dict["Congress Reel"]],
        []
    ),
    Set(
        'reel',
        [tune_dict["Over the Moor to Maggie"],tune_dict["Trip to Durrow"]],
        []
    ),
    Set(
        'reel',
        [tune_dict["Frank's Reel"]],
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
        [AudioReferences("Kesh - Morrison's - Tripping Up the Stairs (unaccompanied)","flute", "Kesh - Morrsion - Tripping - flute - 100 bpm.mp3")]
    ),
    Set(
        'jig',
        [tune_dict["Larry O'Gaff's"], tune_dict["Geese in the Bog"], tune_dict["Jimmy Ward's"]],
        []
    ),
    Set(
        'jig',
        [tune_dict["Connaughtman's Rambles"], tune_dict["Pipe On The Hob"]],
        [AudioReferences("Connaughtman's Rambles - Pipe On the Hob (unaccompanied)", "flute","Conn - Pipe On the Hob - flute - 100 bpm.mp3")]
    ),
    Set(
        'jig',
        [tune_dict["Thrush in the Straw"], tune_dict["Lark on the Strand"]],
        []
    ),
    Set(
        'jig',
        [tune_dict["Trip to the Cottage"],tune_dict["Calliope House"]],
        []
    ),
    Set(
        'jig',
        [tune_dict['Sweets of May'],tune_dict['Lonesome Jig, The'],tune_dict['Rolling Wave, The']],
        []
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
    Set(
        'slip jig',
        [tune_dict["High Road to Kilkenny"],tune_dict["Cock and the Hen"],tune_dict["Blast of Wind"]],
        []
    ),
    Set(
        'slip jig',
        [tune_dict['Kid on the Mountain']],
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
        'polka',
        [tune_dict["Ballydesmond Polka 1"],tune_dict["Egan's"],tune_dict["Ballydesmond Polka 2"]],
        []
    ),
    Set(
        'polka',
        [tune_dict["Farewell to Whiskey"],tune_dict["Lakes of Sligo"], tune_dict["John Ryan's Polka"]],
        []
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
    Set(
        'slide',
        [tune_dict["Where's the Cat"], tune_dict["The Cat's Rambles to the Child's Saucepan"]],
        []
    ),
    # Hornpipe
    Set(
        'hornpipe',
        [tune_dict["Stack of Barley, The"],tune_dict["Bantry Bay"]],
        []
    ),
    Set(
        'hornpipe',
        [tune_dict["Peacock's Feather, The"],tune_dict["Chief O'Neill's"]],
        []
    ),
    Set(
        'hornpipe',
        [tune_dict["Her Long Golden Hair"],tune_dict["Scully Casey's"]],
        []
    ),
    Set(
        'hornpipe',
        [tune_dict["Humours of Tuamgraney"],tune_dict["Walsh's"]],
        []
    ),
    # MAZURKA
    Set(
        'mazurka',
        [tune_dict["Shoe The Donkey"]],
        []
    ),
    Set(
        'mazurka',
        [tune_dict["Sonny's Mazurka"],tune_dict["Irish Mazurka, The"]],
        []
    ),
    # WALTZES
    Set(
        'waltz',
        [tune_dict["South Wind"]],
        []
    ),
    Set(
        'waltz',
        [tune_dict["Si Beag Si Mor"]],
        []
    ),
    Set(
        'waltz',
        [tune_dict["Planxty Hewlett"],tune_dict["Planxty Irwin"]],
        []
    ),
    Set(
        'waltz',
        [tune_dict["Johsefins Dopvals"]],
        []
    ),
    # MARCHES
    Set(
        'march',
        [tune_dict['Bonaparte Crossing the Alps'],tune_dict["Battle of Aughrim"]],
        []
    ),
    # Hop Jigs
    Set(
        'hop jig',
        [tune_dict["Foxhunter's"],tune_dict["Cucanandy"],tune_dict["Dusty Miller, The"]],
        []
    ),
        Set(
        'hop jig',
        [tune_dict["Comb Your Hair and Curl It"],tune_dict["Johnny McGreevy's"]],
        []
    ),
    # Set Dance
    Set(
        'set dance',
        [tune_dict["King of the Fairies"]],
        []
    ),
    Set(
        'set dance',
        [tune_dict["Blackbird"]],
        []
    ),
        Set(
        'set dance',
        [tune_dict["Three Sea Captians"]],
        []
    ),
        Set(
        'set dance',
        [tune_dict["Piper Through the Meadow Straying"]],
        []
    ),
        Set(
        'set dance',
        [tune_dict["Vanishing Lake"]],
        []
    ),
        Set(
        'set dance',
        [tune_dict["Orange Rogue"]],
        []
    ),
        Set(
        'set dance',
        [tune_dict["St. Patrick's Day in the Morning"]],
        []
    ),
        Set(
        'set dance',
        [tune_dict["Humors of Bandon"]],
        []
    ),
]