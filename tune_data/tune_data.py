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
    [AudioReferences("Cooley's","flute","Cooley's - Flute - 80 bpm.mp3")]
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
    [YoutubeVideoEmbed("Lannigan's Ball", "banjo", "https://www.youtube.com/embed/sjFM3hx-fNU")],
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
    """T: Scattery Island
C: Arr: Julia Clifford
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
T: The Tuar Mor, The Toormore
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
  A2FA BAFA|A2FA BAFA|B2cA BAcA|B2cA BAFG |
  A2FA BAFA|A2FA BAFE|FABc d2dB|AFEF D2FG:|
|:Add2 Add2|AddA BAFA|B2cA BAcA|BAcA BAFG |
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
R: Reel
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
R: Reel
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
  [
    AudioReferences("Ships Are Sailing (slow)","concertina","09 Ships Are Sailing (slow).mp3")
  ]
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
  ),
#-----------------------------------------------------------------
  Tune(
    "I Looked East And I Looked West",
    "polka",
    """T:I Looked East And I Looked West
R:Polka
M:2/4
L:1/8
K:G
GB BA/G/|FA AB/A/|GA Bc|   d2 cA     |
GA BA/G/|FA A>B  |cA FA|1) G2 GD    :|2) G2 GB/c/||
dg fe   |fA A>B  |cd ef|   g2 fe     |
dg fe   |fA A>B  |cA FA|1) G2 GB/c/ :|2) g2 GD||""",
    [],
    []
  ),
#-----------------------------------------------------------------
  Tune(
    "Julia Clifford's",
    "polka",
    """T:Julia Clifford's
R:Polka
M:2/4
L:1/8
K:D
f>a ge|f>a ge |fd ed      |  e/f/e/d/ Bd    |
f>a ge|f>a ge |fd e/f/e/c/|1)d2       de   :|2) d2 dB||
A2 A>B|Af  a>f|ed ef/e/   |  dA       Bd/B/ |
A2 AF |Af  a>f|ed ef/e/   |1)d2       dB   :|2) d2 d2||""",
    [],
    []
  ),
#-----------------------------------------------------------------
  Tune(
    "Scartaglen",
    "polka",
    """T:Scartaglen
R:Polka
M:2/4
L:1/8
K:G
GG/G/ GA      |Bd de/f/   |gB B/A/G/A/|  BA A2    |
G>A   GA      |Bd de/f/   |gd AB/A/   |1)G2 GD   :|2)G2 BB/A/||
Gg    g2      |fe e/f/g/e/|dB B/A/G/A/|  BA AB/A/ |
Gg    g2      |fe e/f/g/e/|dB AB/A/   |1)G2 BB/A/ |2)G2 GA/B/||
g2    a2      |b2 ba      |g2 a2      |  b2 ba    |
gb    e/f/g/e/|dB g>e     |dB AB/A/   |1)G2 GA/B/ |2)G2 BB/A/||G4|""",
    [],
    []
  ),
#-----------------------------------------------------------------------
  Tune(
    "Vanishing Lake",
    "set dance",
    """T: Vanishing Lake
C: Michael Fitzpatrick
N: A Part 14 Bars (x2), B Part 18 Bars
R: Set Dance
M: 6/8
L: 1/8
K: Am
|:e/d/|cBc ABc|BAB G>AB|cBc dcd|e3     e2g    |a2a age|
       gag g2e|f2g fed |e3  e2d|c2A    BAG    |A3  Aed|
       c2A BAG|E3  Eed |cee Bee|AA/A/A A2    :|
  E/E/|EAA EAA|EBB EBB |E2c cBA|B3     B2E/E/ |
       EAA EAA|EBB EBB |cBc deg|e3     ec'b   |
       a2a age|gag g2e |f2g fed|e3     e2d    |c2A BAG|
       A3  Aed|c2A BAG |E3  Eed|cee    Bee    |AA/A/A A2|""",
      [],
      [AudioReferences("Vanishing Lake","concertina (midi)","Vanishing Lake - Dotted Eight 75 bpm.mp3")]
  ),
#-------------------------------------------------------------
  Tune(
    "Denis Murphy's",
    "slide",
    """T: Denis Murphy's
R: Slide
M: 12/8
L: 1/8
K: D
|:A2D FED F2A A2f|g2e f2d e2d Bcd|
  A2D FED F2A A2f|a2f efe d3  d3:|
|:d2e f3  gfe f3 |gfe fed e2d Bcd|
  d2e f3  gfe f2f|a2f efe d3  d3:|""",
  [],
  []
  ),
#--------------------------------------------------------------
  Tune(
    "O'Keefe's",
    "slide",
    """T: O'Keefe's
R: Slide
M: 12/8
L: 1/8
K: Ador
|:A2e e2d BAB d2B|A2e e2d B2G GAB|
  A2e e2d BAB d3 |BAB d2e B2A A3:|
|:e2a a2b a2g e2d|efg a2b a2g e2f|
  g3  gfe dBA G3 |BAB d2e B2A A3:|""",
  [],
  []
  ),
#-----------------------------------------------------
  Tune(
    "Going to the Well For Water",
    "slide",
    """T: Going To The Well For Water
R: Slide
M: 12/8
L: 1/8
K: Dmaj
A2f A2f A2f fed|B2g B2g B2g gfe|
cdc BcB Ace a2f|1 g2e cde d3 dcB:|2 g2e cde d3 d2e||
|:f2f fed e2e edc|d2d dcB c2c cBA|
GBB GBB FAA FAA|1 EDE e2d cBc d2e:|2 EDE e2d cBc d3||""",
  [],
  []
  ),
#--------------------------------------------------------
  Tune(
    "Kesh",
    "jig",
    """T: The Kesh
R: Jig
M: 6/8
L: 1/8
K: Gmaj
|:G3 GAB|A3 ABd|edd gdd|edB dBA|
  G3 GAB|A3 ABd|edd gdB|AGF G3:|
|:B3 dBd|ege dBA|B2B dBG|A3 AGA|
  B3 dBd|ege dBd|g3 aga|bgf g3:|""",
  [],
  []
  ),
#-------------------------------------------------------
  Tune(
    "Morrison's",
    "jig",
    """T: Morrison's
R: Jig
M: 6/8
L: 1/8
K: Edor
|:E3 B3|EBE AFD|EDE B3|dcB AFD|
E3 B3|EBE AFD|G3 FGA|dAG FED:|
Bee fee|aee fee|Bee fee|a2g fed|
Bee fee|aee fee|gfe d2A|BAG FGA|
Bee fee|aee fee|Bee fee|faf def|
g3 gfe|def g2d|edc d2A|BAG FED|""",
  [],
  []
  ),
#------------------------------------------------
  Tune(
    "Tripping Up the Stairs",
    "jig",
    """T: Tripping Up the Stairs
R: Jig
M: 6/8
L: 1/8
K: Dmaj
|:FAA GBB|FAd fed|cBc ABc|dfe dAG|
FAA GBB|FAd fed|c2c ABc|1)dfe d2A:|2)dfe dBc||
|:dBB fBB|f3 fed|cAA eAA|e3 edc|
dBB fBB|f3 fed|cBc ABc|1)dfe dBc:||2)dfe d2A||""",
  [],
  []
  ),
#------------------------------------------------
  Tune(
    "Connaughtman's Rambles",
    "jig",
    """T: Connaughtman's Rambles
R: Jig
M: 6/8
L: 1/8
K: Dmaj
|:FAA dAA|BAB dAG|FAA dfe|  d2B BAG |
  FAA dAA|BAB def|gfe dfe|1 d2B BAG:|2 d2B B2g||
|:fbb faa|fef ded|fbb faa|  fed e3  |
  fbb faa|fef def|gfe dfe|1 d2B B2g:|2 d2B BAG||""",
  [],
  []
  ),
#------------------------------------------------
  Tune(
    "Pipe On The Hob",
    "jig",
    """T: The Pipe On The Hob
R: jig
M: 6/8
L: 1/8
K: Dmix
A|: d^cd A2G |F2D DED |EDE cBc|  E2D DFA  |
    dcB cBA  |BAG A2G |EDE cBc|1 E2D D2A :|2 E2D D2e||
 |: f2d d^cd |f2d d^cd|edB c2d|  ede age  |
 [1 f2d d^cd |f2d d^cd|ede age|  ed^c d2e:|
 [2 ~f3 ~g3  |agf g2e |fed eag|  ed^c d2A||
""",
  [],
  [AudioReferences("Pipe On the Hob - Slow","fiddle (Justin Bonar-Bridges)","F - PipeOnTheHob (slow).mp3")]
  ),
]

tune_list_alphab: list[Tune] = sorted(tune_list, key=lambda x: x.title)
tune_dict: dict[str, Tune] = {tune.title: tune for tune in tune_list}