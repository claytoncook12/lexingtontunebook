from tune_data.model.tune import Tune, YoutubeVideoEmbed, AudioReferences

tune_list: list[Tune] = [
  Tune(
    "Cooley's",
    "reel",
    """T: Cooley's
R: Reel
M: 4/4
L: 1/8
K: Edor
|:D2|"Em"EBBA B2EB|B2AB dBAG|"D"FDAD BDAD|FDFA BAGF|
"Em"EBBA B2EB|B2AB defg|"D"afec dBAF|DEFD "Em"E2:|
|:gf|"Em"eBB2 eBgB|eBB2 gedB|"D"A2FA DAFA|A2FA defg|
"Em"eBB2 eBgB|eBB2 defg|"D"afec dBAF|DEFD "Em"E2:|""",
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "Wise Maid, The",
    "reel",
    """T: The Wise Maid
R: Reel
M: 4/4
L: 1/8
K: Dmaj
|:"D"F3G FEDE|FAAB AFED|d2eg fdec|dBAG "A"BEE2|
"D"F3G FEDE|FAAB AFED|d2eg fdec|1) "A"dBAG "D"FDD2:||2) "A"dBAG "D"FDFA||
|:"D"d2AG FDFA|dfaf "A"gfeg|"D"fAdf "A"eAce|"G"dfed "A"cAA2|
"G"BDGB "D"ADFA|dfaf gfed|"G"Bdce "D"dBAG|"A"FGEF "D"D2FA:||"A"FGEF "D"D4||""",
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "Lanigan's Ball",
    "jig",
    """T: Lanigan's Ball
R: Jig
M: 6/8
L: 1/8
K: Edor
|:D|"Em"EFE G2A|B2A Bcd|"D"DED F2G|ABA AFD|
"Em"EFE G2A|B2A Bcd|"C"edB =cBA|"Bm"BGE "Em"E2:|
|:d|"Em"e2f gfe|"D"fag fed|"Em"e2f gfe|fdB "Bm"B2d|
"Em"e2f gfe|"D"fag fed|"C"edB =cBA|"Bm"BGE "Em"E2:|""",
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "Whistling Postman, The",
    "jig",
    """T: The Whistling Postman
C: Charlie Mulvihill
R: Jig
M: 6/8
L: 1/8
K: Dmaj
|:e|"D"f2f edB|AFA BAF|DFA dfa|baf "A"ede|
"D"f2f edB|AFA BAF|DFA "G"BAB|"A"cBc "D"d2:|
|:e|"D"f2f afd|"G"gef gag|"D"fdf afa|baf "A"ede|
"D"f2f edB|AFA BAF|DFA "G"BAB|"A"cBc "D"d2:|""",
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "Out On The Ocean",
    "jig",
    """T: Out On The Ocean
R: Jig
M: 6/8
L: 1/8
K: Gmaj
|:"G"D2B BAG|BdB "D"ABA|"G"GED G2A|"C"B2B "D"AGE|
"G"D2B BAG|BdB "D"ABA|"G"GED G2A|1 "C"BGF "G"GFE:|2 "C"BGF "G"GBd||
|:"Em"e2e edB|ege edB|"D"d2d dBA|ded dBA|
"G"G2A B2d|ege "D"dBA|"G"GED G2A|1 "C"BGF "G"GBd:|2 "C"BGF "G"G3||""",
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "Scattery Island",
    "slide",
    """C: Arr: Julia Clifford
R: Slide
M: 12/8
L: 1/8
K: Dmaj
|:"D"F2A d2f F2A d3|"A"e2A cBA eAA cBA|
"D"F2A d2f F2A d3|"A"e2A cBA f2e "D"d3:|
|:"D"faa f2e d3 def|"G"g2f e2d Bcd "A"efg|
"D"faa f2e d3 def|"G"g2f ecA "A"f2e "D"d3:|""",
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "Jack Regan's",
    "slide",
    """T: Jack Regan's
T: The Tuar Mor
C: Arr: Johnny O'Leary
R: Slide
M: 12/8
L: 1/8
K: Bmin
|:"Bm"F2B BAB d2e faf|"A"e2e efe c2e a3|
"Bm"F2B BAB d2e faf|"A"e2d B2A "Bm"B3 B3:|
|:"Bm"f3 "A"efe "Bm"ded "A"cdc|"G"BAB edB "A"AFE EDE|
"Bm"F2B BAB d2e faf|"A"e2d B2A "Bm"B3 B3:|""",
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "A Fig For A Kiss",
    "slip jig",
    """T: A Fig For A Kiss
M: 9/8
L: 1/8
R: Slip Jig
K: Edor
|:"Em"G2B E2B BAG|"D"F2A D2A AGF|"Em"G2B E2B BAG|"D"BdB AGF "Em"E3:|
"Em"g2e g2e edB|"D"f2d dcd fed|"Em"g2e g2e edB|"Bm"dBG ABd "Em"e2f|
"Em"g2e g2e edB|"D"f2d dcd fed|"Em"gfe "D"fed "Em"efg|"Bm"BdB AGF "Em"E3||""",
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "O'Farrell's Welcome to Limerick",
    "slip jig",
    """T: O'Farrell's Welcome to Limerick
C: O'Farrell
N: O'Farrell (first name unknown) published . . .
R: Slip Jig
M: 9/8
L: 1/8
K: Gmaj
|:"D"FGA AFA c2A|BAG FAF GED|FGA AFA "G"d2A|dfe dcA GED:|
|:"D"d^cd ege d2A|d^cd fdf gfg|afa ged "C"c2A|"G"BAG FAF GED:|
|:"D"FGA AFd AFd|AFd AFA GED|FGA AFA "C"c2A|"G"BAG FAF GED:|
|:"D"DED DED "C"c3|c2B c2A GED|"D"DED DED "G"d2A|dfe dcA GED:|
|:"D"d^cd ege "C"=c2A|"D"d^cd fdf "G"gfg|"D"afa ged "C"c2A|"G"BAG FAF GED:| """,
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "Mom's Favorite",
    "slip jig",
    """T: Mom's Favorite
T: The Knocknagree
N: This setting and name comes from Maida McQuinn-Sugrue (b.1933), a student of Padraig O'Keeffe (1887-1963). Maida taught the tune to Terry "Cuz" Teahan (1905-1989) after they had both emigrated to Chicago. Teahan took to calling the tune "Teahan's Favorite", which Maida took umbrage with. She named the tune after her mother, who would always "dance around the kitchen" whenever she played it. Julia Clifford (1914-1997), also a student of O'Keeffe, recorded it as The Knocknagree.
R: Slide
M: 12/8
L: 1/8
K: Dmaj
|:B|"Em"efe B2A GFE B2 A|"D"FED A2D d2F A2B|
"Em"efe B2A GFE B2A|"D"FED FAF "Em"E3 E2:|
|:A|"Em"B2e ede "D"f2a afa|"Bm"baf g2f e2d B2A|
"Em"B2e ede "D"f2a afa|"Bm"baf g2f "Em"e3 e2d|
"Em"B2e ede "D"f2a afa|"Bm"baf g2f e2d B2g|
"D"faf f2e efe B2A|FED FAF "Em"E3 E3||""",
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "Brosna, The",
    "slide",
    """T: The Brosna
R: Slide
M: 12/8
L: 1/8
K: Gmaj
|:"G"D2G G2A BAB d2B|"D"A2D FED A2D FED|
"G"D2G G2A BAB d2B|1 "D"A2D FED "G"G3 G2E:|2 "D"A2D FED "G"G3 GBd||
|:"G"g2f efg f2e d2B|"C"c2B A2B c2d "D"e2f|
"G"g2f efg f2e d2B|1 "C"c2A "D"F2A "G"G3 GBd:|2 "C"c2A "D"F2A "G"G3 G3|| """,
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "Shoe The Donkey",
    "mazurka",
    """T: Shoe The Donkey
R: Mazurka
M: 3/4
L: 1/8
K: Gmaj
DG|:"G"B2 B2 DG|B2 B2 DG|B2 c2 B2|"D"A4 DF|
A2 A2 DF|A2 A2 DF|A2 B2 A2|1 "G"G4 DG:|2 "G"G3 ABc||
|:"G"d2 g2 f2|"D"A3 GAB|c2 e2 d2|"G"B4 Bc|
B2 A2 B2|"C"c3 Bcd|1 e2 d2 c2|"G"B3 ABc:|2 e2 d2 "D"F2|"G" G4|| """,
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "Barony Jig, The",
    "slip jig",
    """T: The Barony Jig
S: O'Neill - Dance Music of Ireland: 1001 Gems (1907), No. 970
R: Slip Jig
M: 9/8
L: 1/8
K: Am
|:B|c2A c2A AGE|c2A ABd e2d|c2A c2A AGE|GED DEG A2B|
c2A c2A AGE|c2A ABd e2d|c2A efd cBA|GED DEG A2:|
|:B|c2d ecA AGE|c2d efd e2d|c2d ecA AGE|GED DEG A2B|
c2d ecA AGE|c2d efd e2e|cde ged ecA|GED DEG A2:||""",
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    "Snowy Path, The",
    "slip jig",
    """T: The Snowy Path
C: Mark Kelly
R: slip jig
M: 9/8
L: 1/8
K: Dmaj
|"D"F2A B2F A2F|"G"G2B d2e dBA|"D"F2A B2F A2F|"Em"E2D E2F GFE|
"D"F2A B2F A2F|"G"G2B d2e dBA|"D"F2A B2F A2F|"Em"E2D E2F GAB||
"A"c3 c2e d2c|"G"B2G B2c d2e|"Bm"f3 f2e d2B|"D"A2G F2G A2B|
"A"c3 c2e d2c|"G"B2G B2c d2e|"D"d2A B2F A2F|"Em"E2D E2F GFE||""",
    [],
    []
  ),
#--------------------------------------------------------------
  Tune(
    'Concertina Reel',
    'reel',
    """T: Concertina Reel
R: reel
M: C|
K: D
  "^A Part" A2FA BAFA|A2FA BAFA|B2cA BAcA|B2cA BAFG |
  A2FA BAFA|A2FA BAFE|FABc d2dB|AFEF D2FG:|
|:"^B Part" Add2 Add2|AddA BAFA|B2cA BAcA|BAcA BAFG |
  Add2 Add2|AddA BAFE|FABc d2dB|AFEF D4  :|""",
    [
      YoutubeVideoEmbed("Foinn Seisiun 1 CD's", 'accordion, banjo, concertina, fiddle, flute', 'https://www.youtube.com/embed/j1mfZ15mPeA'),
      YoutubeVideoEmbed("Hatao's Irish Tune of the Day #131", 'flute', 'https://www.youtube.com/embed/v0EMMbo9ikw')
    ],
    [
      AudioReferences('Slow Playing of the Concertina Reel', 'concertina', '08 The Concertina (slow).mp3')
    ]
  ),
#--------------------------------------------------------------    
  Tune(
    'Merry Blacksmith',
    'reel',
    """T: Merry Blacksmith
R: reel
M: C|
K: G
  d2dA BAFA|ABdA BAFA|ABde f2ed|Beed e2fe |
  d2dA BAFA|ABdA BAFA|ABde f2ed|BAFE D4  :|
|:a2ag f2fe|d2dA BAFA|ABde f2ed|BAFE efge |
  a2ag f2fe|d2dA BAFA|ABde f2ed|BAFE D4  ||""",
  [
    YoutubeVideoEmbed("Foinn Seisiun 1 CD's", 'accordion, banjo, concertina, fiddle, flute', 'https://www.youtube.com/embed/dJz8TPijdXk'),
    YoutubeVideoEmbed("Hatao's Irish Tune of the Day #151", 'flute', 'https://www.youtube.com/embed/pIQXhPhzEXE')
  ],
  []
  ),
#--------------------------------------------------------------    
  Tune(
    'Sally Gardens',
    'reel',
    """T: Sally Gardens
R: reel
M: C|
K: G
BA| G2DG B2GB|dBeB dBAB|d2Bd efge|   dBAB GEDE |
    G2DG B2GB|dBeB dBAB|d2Bd efge|1) dBAB G2BA:|2) dBAB GABc||
  |:dggf g2de|g2bg aged|eaag a2eg|   a2bg ageg |
    dggf g2de|g2bg ageg|d2Bd efge|1) dBAB GABc:|2) dBAB G2BA||""",
  [
    YoutubeVideoEmbed("Foinn Seisiun 1 CD's", 'accordion, banjo, concertina, fiddle, flute', 'https://www.youtube.com/embed/ohQ2cF4H6NE'),
    YoutubeVideoEmbed("Hatao's Irish Tune of the Day #11", 'flute', 'https://www.youtube.com/embed/ispQQ5GMzjc'),
    YoutubeVideoEmbed("Banjo Buddy", "banjo", "https://www.youtube.com/embed/TuONrq0tQSo")
  ],
  []
  ),
#---------------------------------------------------------------
  Tune(
    "Ships are Sailing",
    "reel",
    """T: Ships are Sailing
R: reel
M: C|
K: Em
"Em"Beed BcdB|"D"ADFD ADFA|"Em"E3F "D/F#"GFGA|"G"Beef "D"gfed|
"Em"Beed BcdB|"D"ADFD ADFA|"Em"E3F GFGA|1) "Em"Beed e4:|2) "Em"Beed e3f||
"Em"g3a  bgeg|"D"f2fg afdf|"Em"gfga bgeg|"D"fede "Em"e3f|
"Em"g2ga bgeg|"D"fefg afdf|"G"g2bg "D/F#"fgaf|1) "Em"edef "D"gfef:|2) "Em"edef "D"gfed||""",
  [],
  []
  ),
#----------------------------------------------------------------
  Tune(
    "Father Kelly's",
    "reel",
    """T: Father Kelly's
R: Reel
M: C|
K:G
"G"B2GB AGEG|"G"DGGF G2AB|"C"cBAB  cBAG|"D"EAAG FDGA|
"G"B2GB "D/F#"AGEG|"G"DGGE "G/B"GABc|"C"d2Bd  gdBd|1) "D"cFEF "G"G3A :|2) "D"cAFA "G"GABc||
"G"d2Bd gdBd|dGBd gdBd|"A"e2^ce "A/C#"agfe|"D"defg agfe|
"G"d2Bd gdBd|"G/B"dGBd gdBd|"C"c2Ac  "Am"BAGB|1) "D"AGFA "G"GABc :|2) "D"AGFA "G"G3A||""",
    [],
    []
  )
]

tune_list_alphab: list[Tune] = sorted(tune_list, key=lambda x: x.title)
tune_dict: dict[str, Tune] = {tune.title: tune for tune in tune_list}