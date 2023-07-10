from tune_data.model.tune import Tune, YoutubeVideoEmbed, AudioReferences

tune_list: list[Tune] = [
  Tune(
    "Cooley's",
    "reel",
    "Edor",
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
    [AudioReferences("Cooley's","flute","Cooley's - Flute - 80 bpm.mp3")],
    notes_complete = True,
    chords_complete= True
  ),
#--------------------------------------------------------------
  Tune(
    "Wise Maid, The",
    "reel",
    "D",
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
    [AudioReferences("Wise Maid - slow","concertina","14 The Wise Maid (slow).mp3")]
  ),
#--------------------------------------------------------------
  Tune(
    "Lanigan's Ball",
    "jig",
    "Edor",
    """T: Lanigan's Ball
R: Jig
M: 6/8
L: 1/8
K: Edor
|:D|"Em"EFE G2A|B2A Bcd|"D"DED F2G|ABA AFD|
"Em"EFE G2A|B2A Bcd|"C"edB =cBA|"Bm"BGE "Em"E2:|
|:d|"Em"e2f gfe|"D"fag fed|"Em"e2f gfe|fdB "Bm"B2d|
"Em"e2f gfe|"D"fag fed|"C"edB =cBA|"Bm"BGE "Em"E2:|""",
    [YoutubeVideoEmbed("Lanigan's Ball", "banjo", "https://www.youtube.com/embed/sjFM3hx-fNU")],
    [AudioReferences("Lanigan's Ball medium tempo", "flute", "Lanigan's Ball - flute - 80 bpm.mp3")],
    notes_complete = True,
    chords_complete = True
  ),
#--------------------------------------------------------------
  Tune(
    "Whistling Postman, The",
    "jig",
    "D",
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
    [AudioReferences("Whistling Postman - 80 bpm","flute","Whistling Postman - flute - 80 bpm.mp3")],
    notes_complete = True,
    chords_complete = True
  ),
#--------------------------------------------------------------
  Tune(
    "Out On The Ocean",
    "jig",
    "G",
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
    [AudioReferences("Out on the Ocean 80 bpm","flute","Out on the Ocean - flute - 80 bpm.mp3")],
    notes_complete = True,
    chords_complete = True
  ),
#--------------------------------------------------------------
  Tune(
    "Scattery Island",
    "slide",
    "D",
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
    [],
    notes_complete=True,
    chords_complete=True
  ),
#--------------------------------------------------------------
  Tune(
    "Jack Regan's",
    "slide",
    "Bmin",
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
    [AudioReferences("Jack Regan's","flute","Toormore Slide - Flute.mp3")],
    notes_complete=True,
    chords_complete=True
  ),
#--------------------------------------------------------------
  Tune(
    "A Fig For A Kiss",
    "slip jig",
    "Edor",
    """T: A Fig For A Kiss
M: 9/8
L: 1/8
R: Slip Jig
K: Edor
|:"Em"G2B E2B BAG|"D"F2A D2A AGF|"Em"G2B E2B BAG|"D"BdB AGF "Em"E3:|
"Em"g2e g2e edB|"D"f2d dcd fed|"Em"g2e g2e edB|"Bm"dBG ABd "Em"e2f|
"Em"g2e g2e edB|"D"f2d dcd fed|"Em"gfe "D"fed "Em"efg|"Bm"BdB AGF "Em"E3||""",
    [],
    [],
    notes_complete=True,
    chords_complete=True
  ),
#--------------------------------------------------------------
  Tune(
    "O'Farrell's Welcome to Limerick",
    "slip jig",
    "Dmix",
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
    [AudioReferences("O'Farrell's Welcome to Limerick","fiddle bouzouki","2023-06-25 O'Farrell's Welcome to Limerick.mp3")],
    notes_complete=True,
    chords_complete=True
  ),
#--------------------------------------------------------------
  Tune(
    "Mom's Favorite",
    "slip jig",
    "D",
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
    [AudioReferences("Mom's Favorite","fiddle","2023-06-25 Mom's Favorite Fiddle.mp3")],
    notes_complete=True,
    chords_complete=True
  ),
#--------------------------------------------------------------
  Tune(
    "Brosna, The",
    "slide",
    "G",
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
    [],
    notes_complete=True,
    chords_complete=True
  ),
#--------------------------------------------------------------
  Tune(
    "Shoe The Donkey",
    "mazurka",
    "G",
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
    [],
    notes_complete=True,
    chords_complete=True
  ),
#--------------------------------------------------------------
  Tune(
    "Barony Jig, The",
    "slip jig",
    "Amin",
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
    [AudioReferences("The Barony Jig - slow", "flute", "The Barony Jig - flute - 80 bpm.mp3")],
    notes_complete=True
  ),
#--------------------------------------------------------------
  Tune(
    "Snowy Path, The",
    "slip jig",
    "D",
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
    [],
    notes_complete=True,
    chords_complete=True
  ),
#--------------------------------------------------------------
  Tune(
    'Concertina Reel',
    'reel',
    'D',
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
    ],
    notes_complete=True
  ),
#--------------------------------------------------------------    
  Tune(
    'Merry Blacksmith',
    'reel',
    'D',
    """T: Merry Blacksmith
R: Reel
M: C|
K: D
  d2dA BAFA|ABdA BAFA|ABde f2ed|Beed e2fe |
  d2dA BAFA|ABdA BAFA|ABde f2ed|BAFE D4  :|
|:a2ag f2fe|d2dA BAFA|ABde f2ed|BAFE efge |
  a2ag f2fe|d2dA BAFA|ABde f2ed|BAFE D4  ||""",
    [
      YoutubeVideoEmbed("Foinn Seisiun 1 CD's", 'accordion, banjo, concertina, fiddle, flute', 'https://www.youtube.com/embed/dJz8TPijdXk'),
      YoutubeVideoEmbed("Hatao's Irish Tune of the Day #151", 'flute', 'https://www.youtube.com/embed/pIQXhPhzEXE')
    ],
    [],
    notes_complete=True
  ),
#--------------------------------------------------------------    
  Tune(
    'Sally Gardens',
    'reel',
    'G',
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
      YoutubeVideoEmbed("Hatao's Irish Tune of the Day #11", 'flute', 'https://www.youtube.com/embed/ispQQ5GMzjc')
    ],
    [],
    notes_complete=True,
  ),
#---------------------------------------------------------------
  Tune(
    "Ships are Sailing",
    "reel",
    "Emin",
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
    ],
    notes_complete=True,
    chords_complete=True
  ),
#----------------------------------------------------------------
  Tune(
    "Father Kelly's",
    "reel",
    "G",
    """T: Father Kelly's
R: Reel
M: C|
K:G
"G"B2GB AGEG|"G"DGGF G2AB|"C"cBAB  cBAG|"D"EAAG FDGA|
"G"B2GB "D/F#"AGEG|"G"DGGE "G/B"GABc|"C"d2Bd  gdBd|1) "D"cFEF "G"G3A :|2) "D"cAFA "G"GABc||
"G"d2Bd gdBd|dGBd gdBd|"A"e2^ce "A/C#"agfe|"D"defg agfe|
"G"d2Bd gdBd|"G/B"dGBd gdBd|"C"c2Ac  "Am"BAGB|1) "D"AGFA "G"GABc :|2) "D"AGFA "G"G3A||""",
    [YoutubeVideoEmbed("Father Kelly's Slow Then Faster", "fiddle","https://www.youtube.com/embed/vDzBpuRhsfo")],
    [AudioReferences("Father Kelly's slow","concertina","10 Father Kelly's (slow).mp3")],
    notes_complete=True,
    chords_complete=True
  ),
#-----------------------------------------------------------------
  Tune(
    "I Looked East And I Looked West",
    "polka",
    'G',
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
    [],
    notes_complete=True
  ),
#-----------------------------------------------------------------
  Tune(
    "Julia Clifford's",
    "polka",
    'D',
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
    [],
    notes_complete=True
  ),
#-----------------------------------------------------------------
  Tune(
    "Scartaglen",
    "polka",
    'G',
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
    [],
    notes_complete=True
  ),
#-----------------------------------------------------------------------
  Tune(
    "Vanishing Lake",
    "set dance",
    "Amin",
    """T: Vanishing Lake
C: Michael Fitzpatrick
N: A Part 14 Bars (x2), B Part 18 Bars
R: Set Dance (Jig)
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
    [AudioReferences("Vanishing Lake","concertina (midi)","Vanishing Lake - Dotted Eight 75 bpm.mp3")],
    notes_complete=True
  ),
#-------------------------------------------------------------
  Tune(
    "Denis Murphy's",
    "slide",
    'D',
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
    [],
    notes_complete=True
  ),
#--------------------------------------------------------------
  Tune(
    "O'Keefe's",
    "slide",
    "Ador",
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
    [],
    notes_complete=True
  ),
#-----------------------------------------------------
  Tune(
    "Going to the Well For Water",
    "slide",
    "D",
    """T: Going To The Well For Water
R: Slide
M: 12/8
L: 1/8
K: Dmaj
B|:A2f A2f A2f fed|  B2g B2g B2g gfe |
   cdc BcB Ace a2f|1 g2e cde d3  dcB:|2 g2e cde d3 d2e||
 |:f2f fed e2e edc|  d2d dcB c2c cBA |
   GBB GBB FAA FAA|1 EDE e2d cBc d2e:|2 EDE e2d cBc d3||""",
    [],
    [],
    notes_complete=True
  ),
#--------------------------------------------------------
  Tune(
    "Kesh",
    "jig",
    None,
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
    "Edor",
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
    [],
    notes_complete=True
  ),
#------------------------------------------------
  Tune(
    "Tripping Up the Stairs",
    "jig",
    "D",
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
    [],
    notes_complete=True
  ),
#------------------------------------------------
  Tune(
    "Connaughtman's Rambles",
    "jig",
    "D",
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
    [],
    notes_complete=True
  ),
#------------------------------------------------
  Tune(
    "Pipe On The Hob",
    "jig",
    "Dmix",
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
  [AudioReferences("Pipe On the Hob - Slow","fiddle","F - PipeOnTheHob (slow).mp3")],
  notes_complete=True
  ),
#------------------------------------------------
  Tune(
    "Little Fair Canavans",
    "slip jig",
    "G",
    """T: Little Fair Canavans
R: Slip Jig
M: 9/8
L: 1/8
K: G
|:  A|BAG AGE GED|EGD DEG A2c|BAG AGE GED|EGD DEF G2:|
|:  A|Bdd edd BAG|Bdd edB A2c|Bdd edd BAG|GED DEF G2:|
""",
  [],
  [AudioReferences("Fair Little Canavans (slow then faster)","flute","01_Flute_Cannavans.mp3")],
  notes_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Redigan's Mother",
    "slip jig",
    "D",
    """T: Redican's Mother
R: slip jig
M: 9/8
L: 1/8
K: Dmaj
  A|FAA FAd AFD|FAA FAd B2A|FAA FAd AFD|EDB, DFA B2:|
|:e|f3 faf edB|Aff fef g2e |f3 faf edB|AFE DFA B2 :|""",
  [],
  [AudioReferences("Redican's Mother","flute","redican's mother - flute.mp3")],
  notes_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Humours of Derrycrossane",
    "slip jig",
    "G",
    """T: Humours of Derrycrossane
R: slip jig
M: 9/8
L: 1/8
K: G
G|:B2B BAB c2c|BAG BdB ABc|BAG BdB cde|1)dBG GAF G2A:|2) dBG GAF GBd||
 |:g3  edc Bcd|ecA ABG A2d|g2g edc Bcd|  gdB GAF GBd |
   g3  edc Bcd|ecA ABG A2B|def gfe def|  gbg agf gdc ||  B3""",
  [],
  [AudioReferences("Humours of Derrycrossane","flute","Humours of Derrycrossane - flute.mp3")],
  notes_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Larry O'Gaff's",
    "jig",
    "D",
    """T: Larry O'Gaff's
R: Jig
M: 6/8
L: 1/8
K: Dmaj
A|:d2D FED|ABA AFD|GBG    FAF|  EFG ABc |
   d2D FED|ABA AFD|GBG    FAF|1)EFE D2A:|2)EFE D3 ||
 |:ABc d3 |efe edB|AB/c/d ede|  fdc dcB |
   ABc d3 |ABA AFD|G3     FGF|1)EFE D3 :|2)EFG ABc||d3""",
  [],
  [AudioReferences("Larry O'Gaff Feb 26, 2023 Session","fiddle, mandolin, bouzouki","Larry O'Gaff's - session - 2023-02-26.mp3")],
  notes_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Geese in the Bog",
    "jig",
    "C",
    """T: The Geese In The Bog
R: Jig
M: 6/8
L: 1/8
K: Ador
  B|cEE GEE|cEE GAB|cEE GED|E2A A2B |
    cEE GEE|cEE GAB|cBA GED|E2A A2 :||
|:B|cde ged|e2a ged|cde ged|e2a a3  |
    cde ged|e2a ged|cBA GED|E2A A2 :|""",
  [],
  [AudioReferences("Geese in the Bog - Slow","flute","Geese in the Bog - flute- 80 bpm.mp3")],
  notes_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Jimmy Ward's",
    "jig",
    "G",
    """T: Jimmy Ward's
R: Jig
M: 6/8
L: 1/8
K: Gmaj
|:G3  GAB|AGE GED|G3  AGE|  GED DEF|
  G3  GAB|AGE GAB|cBA BGE|1)DED DEF:|2)DED D2B||
|:cBA BAG|A3 AGE|cBA  BGE|  DED GAB|
  cBA BAG|A2A ABc|dcA AGE|1)GED D2B:|2)GED DEF||G6||""",
  [],
  [],
  notes_complete=True
  ),
#---------------------------------------------------
  Tune(
    "South Wind",
    "waltz",
    "G",
    """T: South Wind
R: Waltz
M: 3/4
L: 1/8
K: Gmaj
dc|: B3A G2|B3c d2   |  A3 BA2|A4 dc    |
     B3A G2|E3D E2   |1)G6    |G4 dc   :|2)G6|G4 (3def||
  |: g4  g2|g2  f2 e2|  d3 ed2|d4   c2  |
     B3A G2|B3c d2   |  A3 BA2|A4 (3def |
     g4  g2|g2  f2 e2|  d3 ed2|d4   c2  |
     B3A G2|Bc3 GA   |  G6-   |G6      :|
""",
  [],
  [],
  notes_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Si Beag Si Mor",
    "waltz",
    "D",
    """T: Si Beag Si Mor
R: Waltz
M: 3/4
L: 1/8
K: Dmaj
de|:f3e d2|d3e d2|B4 A2|F4 A2|BA Bc d2|e4 de|f2 f2 e2|
d4 f2|B4 e2|A4 d2|F4 E2|D4 f2|B4 e2|A4 dc|d6|d4 de:|
|:f2 fe d2|ed ef a2|b4 a2|f4 ed|e2 e2 a2|f4 e2|d4 B2|B4 BA|
F4 E2|D4 f2|B4 e2|A4 a2|ba gf ed|e4 dc|d6|1 d4 de:|2 d6||
""",
  [],
  [],
  notes_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Cook in the Kitchen, The",
    "jig",
    "G",
    """T: The Cook In The Kitchen
R: Jig
M: 6/8
L: 1/8
K: Gmaj
|:DGG GAG|FDE =F2E|D2G GFG|A2 d cAF|
DGG GAG|FDE =F2 d|cAG FGA|1 BGF G2E:|2 BGF G2A||
|:B2B BAG|A2A AGF|G2G GFG|A2 d cAG|
B2B BAG|A2A A2 d|cAG FGA|1 BGF G2A:|2 BGF G2B||
|:d2 e f2 g|a2 g fed|cAG FGA|B2B cAF|
d2 e f2 g|a2 g fed|cAG FGA|1 BGF G2B:|2 BGF G3||
""",
  [],
  [AudioReferences("Cook in the Kitchen - 80 bpm","flute","Cook in the Kitchen - flute - 80 bpm.mp3")],
  notes_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Rambling Pitchfork",
    "jig",
    "D",
    """T: The Rambling Pitchfork
R: Jig
M: 6/8
L: 1/8
K: Dmaj
  F2F AFF|dFF AFD|G2G ABc|   ded cAG|
  F2F AFF|dFF AFD|G2G B2B|1) AFD D2E:|2) AFD DFA||
|:d2d fed|ecA ABc|d2d fed|   faf gfe |
  d2d fed|ecA AGF|G2G B2B|1) AFD DFA:|2) AFD D3 ||
""",
  [],
  [AudioReferences("Rambling Pitchfork - 80 bpm","flute","Rambling Pitchfork - flute - 80 bpm.mp3")],
  notes_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Rolling Wave, The",
    "jig",
    "D",
    """T: The Rolling Waves
T: (Humors of Trim)
R: Jig
M: 6/8
L: 1/8
K: Dmaj
E||:"D"F3 DED|D2d cAG|FEF DE/F/G|"A"A2F GFE|
"D"F3 DED|D2d cAG|"D/F#"F3 "G"G3|"A"A2F GFE:|
|:"D"D2d cAd|cAd cAG|"D/C#"F2d cAG|F/G/AF GFE|
"Bm"D2d cde|fed cAG|"D/F#"F3 "G"G3|"A"A2F GFE:|
""",
  [
    YoutubeVideoEmbed("Rolling Wave slow then faster","flute","https://www.youtube.com/embed/4_Oav6Xz8i8"),
    YoutubeVideoEmbed("Rolling Wave","concertina","https://www.youtube.com/embed/lDhVtftIc6E"),
    YoutubeVideoEmbed("Rolling Wave","fiddle","https://www.youtube.com/embed/0JUktG3OZ8Y")
  ],
  [],
  notes_complete=True,
  chords_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Maid Behind the Bar, The",
    "reel",
    "D",
    """T: The Maid Behind The Bar
R: reel
M: C|
L: 1/8
K: Dmaj
|:"D"FAAB AFED|FAAB ABde|"Bm"fBBA Bcde|"Em"f2gf "A"edBG|
"D"FAAB AFED|FAAB ABde|"Bm"fBBA "G"BcdB|"A"AFEF "D"D4:|
|:"D"faag fdde|fdag fd d2|"Em"efga beef|gebe "A"gee2|
"D"faaa "G"b2af|"D"defd "A"e2de|"G"fBBA BcdB|"A"AFEF "D"D4:|
""",
    [
      YoutubeVideoEmbed("Maid Behind the Bar Teaching","flute","https://www.youtube.com/embed/b3elEri-f2w"),
      YoutubeVideoEmbed("Maid Behind the Bar","whistle","https://www.youtube.com/embed/-mYx_T-SCWY"),
      YoutubeVideoEmbed("Maid Behind the Bar slow","whistle","https://www.youtube.com/embed/JbpL6fdrqcM"),
    ],
    [
      AudioReferences("Maid Behind the Bar slow","concertina","11 The Maid Behind the Bar (slow).mp3")
    ],
    notes_complete=True,
    chords_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Cock and the Hen",
    "slip jig",
    "F#min",
    """T: Cock and the Hen
T: Ryan's
R: Slip Jig
M: 9/8
L: 1/8
K: Dmaj
|:"F#m"F3 FEF "A"c2A|"F#m"F3 FEF "E"AFE|"F#m"F3 FEF "A"c2d|1)"E"ecA BAF AFE:|2)"E"ecA BAF AFe||
"A"ecA ABc "D"dzf|"A"ecA ABc "D"BAF|"A"ecA ABc "D"d2z|"E"cBA BAF AFe|
"A"ecA ABc "D"dza|"A"ecA ABc "D"BAF|"A"ecA ABc "D"d2z|"E"cBA BAF AFE|
""",
    [
      YoutubeVideoEmbed("Cock and the Hen slow then faster","fiddle","https://www.youtube.com/embed/FSwijXAW228"),
      YoutubeVideoEmbed("Cock and the Hen (first tune)","flute, fiddle, guitar, bodhran","https://www.youtube.com/embed/hPU6w6jZ_MY")
    ],
    [],
    notes_complete=True,
    chords_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Lonesome Jig, The",
    "jig",
    "D",
    """T: The Lonesome Jig
T: Rolling Waves
R: Jig
M: 6/8
L: 1/8
K: Dmaj
|:"D"F2E EDE|F2D DED|F2E EFA|"G"d2e fdA |
  "D"F2E EDE|F2D DED|"G"AFE EFA|"A"B3  "D"d3 :|
|:"D"ABd e2f|d2c B2A|ABd e2f|"G"d2  AB3 |
  "D"ABd ede|fdB BAF|"G"AFE EFA|"A"B3  "D"d3 :|
""",
    [YoutubeVideoEmbed("The Lonesome Jig - slow then faster", "flute", "https://www.youtube.com/embed/ITyjNak_yoM")],
    [AudioReferences("The Lonesome Jig - 80 bpm", "flute", "Lonesome Jig -flute - 80 bpm.mp3")],
    notes_complete=True,
    chords_complete=True
  ),
#---------------------------------------------------
  Tune(
    "Egan's",
    "polka",
    "D",
    """T: Egan's
T: Peg Ryan's
R: Polka
M: 2/4
L: 1/8
K: Dmaj
|:"D"fA BA|fA BA|"G"d2 e>f|"A"ed BA|"D"fA BA|fA BA|"G"d2 e>f|"A"ed "D"d2:|
|:"D"fa fe|ed BA|"G"d2 e>f|"A"ed BA|"D"fa fe|ed BA|"G"d2 e>f|"A"ed "D"d2:|
""",
    [YoutubeVideoEmbed("Egan's Polka", "accordion, fiddle, flute, banjo", "https://www.youtube.com/embed/rzxQqqD-4AY")],
    [],
    notes_complete=True,
    chords_complete=True
  ),
#------------------------------------------------------
  Tune(
    "Stack of Barley, The",
    "hornpipe",
    "G",
    """T: Stack of Barley, The
R: Hornpipe
M: 2/2
L: 1/8
K: G
|:gf|"C"efed "G/B"B2dB|"Am"AGEG "D"AcBA|"G"GFGA BABd|"D"e2A2 A2gf|
     "C"efed "G/B"B2dB|"D"AGEG     AcBA|"G"GFGA BdAc|"G"B2"D/F#"G2 "G"G2:|
|:GA|"G"BABd    g2fg|"Em"agfg    edBd|"C"g2fg edBd|"D"e2A2 A2fg|
     "D"agfa "C"gedB|"G/B"cBAG "D"AcBA|"G"GFGA Bd Ac|"G"B2"D/F#"G2 "G"G2:|
""",
  [],
  [],
  notes_complete=True,
  chords_complete=True
  ),
#------------------------------------------------------
  Tune(
    "John Ryan's Polka",
    "polka",
    "D",
    """T: John Ryan's Polka
R: Polka
M: 2/4
L: 1/8
K: D
|:"D"dd B/c/d/B/|AF AF   |dd B/c/d/B/|AF ED       |
  "D"dd B/c/d/B/|AF Ad/e/|"G"fd "A"ec|1)"D"d2d2  :|2)"D"d2 de||
|:"D"fd de/f/   |gf ed/e/|fd Ad      |"G"fa a>g   |
| "D"fd de/f/   |gf ed/e/|"G"fd "A"ec|1)"D"d2 d>e:|2)"D"d2d2||
""",
    [],
    [],
    notes_complete=True,
    chords_complete=True
  ),
#------------------------------------------------------
  Tune(
      "Ballydesmond Polka 1",
      "polka",
      'Ador',
      """T: Ballydesmond Polka 1
R: Polka
M: 2/4
L: 1/8
K: Ador
|:EA AB |cd e/f/g|G2 G>A|GE ED |
  EA AB |cd e>g |ge dB|A2 A2:|
|:a2 a>b|ag ef  |g2 g>a|ge ed |
  ea a>b|ag e>f |ge dB|A2 A2:|
""",
  [],
  [],
  notes_complete=True
  ),
#------------------------------------------------------
  Tune(
      "Ballydesmond Polka 2",
      "polka",
      'Ador',
      """T: Ballydesmond Polka 2
R: Polka
M: 2/4
L: 1/8
K: Ador
A/B/|:c2 B2      |AB/A/ G>A  |Bd ed|g2 ed|
    ea g/a/g/e/|dB    GA/B/|ce dB|1)A2 AA/B/:|2)A2 A2||
|:ea ag/e/   |dg gd   |ea ab|g2 ed|
ea g/a/g/e/|dB GA/B/|ce dB|A2 A2:| 
""",
  [],
  [],
  notes_complete=True
  ),
#------------------------------------------------------
  Tune(
      "Kid on the Mountain",
      "slip jig",
      "Eaeol",
      """T: Kid on the Mountain
R: Slip Jig
M: 9/8
L: 1/8
K: Eaeol
E3 FEF GGF|EDE BcA BGD|E3 FEF G2A|BAG F/G/AG FED:|
BGB AFA G2D|GAB dge dBA|BGB AFA G2A|BAG F/G/AG FED:|
gfg eBe e2f|gfg efg afd|gfg eBe g2a|bag f/g/ag fed:|
eBB e2f g3|eBB efg afd|eBB e2f g2a|bag f/g/ag fed:|
edB dBA G2D|GAB dge dBd|edB dBA G2A|BAG F/G/AG FED:|HE3
""",
  [],
  [],
  notes_complete=True
  ),
#------------------------------------------------------
  Tune(
      "King of the Fairies",
      "set dance",
      "Eaeol",
      """T: King of the Fairies
R: Set Dance (Hornpipe)
M: 4/4
L: 1/8
K: Eaeol
B,2|:E>D E>F G>F G>A|B>c B>A G>F G>A|B2 E2 E>F G>E|F>G F>E D2 B,2|
E>D E>F G>F G>A|B>A (3GAB d2- d>c|B2 E2 G>F E>D|1)E2 E>D E2 B,2:|2)E2 E>D E2- E>d||
e2 B2 B>d e>f|g>a g>f e2- e>d|e2 B2 B>A B>^c|d>e d>^c B>c (3dcB|
e2 B2 B>d e>f|g>a g>f e2- e>d|B>d e>g f>e d>f|e2 e>d e2- e>f|
g2 g>e f2 f>d|e>d B>^c d2- d>e|d>B A>F G>A B>^c|d>^c B>A G>F E>D|
B,2 E2 E>F G>A|B2 e2 e>d e>f|e2 B2 B>A G>F| E4 E4||
""",
  [],
  [AudioReferences("King of the Fairies","flute","King of the Faries - flute - 120 bpm.mp3")],
  notes_complete=True
  ),
#------------------------------------------------------
  Tune(
      "Bantry Bay",
      "hornpipe",
      "G",
      """T: Bantry Bay
T: Little Stack of Wheat
R: hornpipe
M: 4/4
L: 1/8
K: Gmaj
GA|:"G"BGAG "C"EGDE|"G"G2"C"GF "G"GBAG|"C"EGAB "D7"cBAG|"Am"E2A2 A3B|
"C"c2cA "G"B2BG|"D7"ABAG "C"E2D2|"G"BGAG "C"EGDE|1 "G"G2"C"GF "G"G2GA:|2 "G"G2"C"GF "G"GABc||
|:"G"dBGB dBGA|"Em"B2e2 e3f|"C"gfed "G"BGBd|"C"(3gag "D7"fa "G"g2g2|
"G"gagf "C"efed|"G"BGAG "C"EGD2|"G"BGAG "C"EG (3DEF|1)"G"G2"C"GF "G"G2Bc:|1)"G"G2"C"GF "G"G4:|
""",
  [],
  [AudioReferences("Bantry Bay slow", "fiddle","F - BantryBay (hornpipe).mp3")],
  notes_complete=True,
  chords_complete=True
  ),
#------------------------------------------------------
  Tune(
    "Blast of Wind",
    "slip jig",
    None,
    """T:Blast of Wind
%%center Need Notes 
""",
    [],
    [AudioReferences("Blast of Wind (Drop of Spring Water)", "fiddle", "2023-06-25 Blast of Wind Fiddle.mp3")]
  ),
#------------------------------------------------------
  Tune(
    "High Road to Kilkenny",
    "slip jig",
    None,
"""T:High Road to Kilkenny
%%center Need Notes 
""",
    [],
    [AudioReferences("High Road to Kilkenny", "fiddle", "2023-06-25 High Road to Kilkenny Fiddle.mp3")]
  ),
#------------------------------------------------------
  Tune(
    "Sweets of May",
    "jig",
    "G",
    """T:Sweets of May
%%center Need Notes 
""",
    [],
    [AudioReferences("Sweets of May", "fiddle", "2023-06-25 Sweets of May Fiddle.mp3")]
  ),
#------------------------------------------------------
  Tune(
    "Devanney's Goat",
    "reel",
    None,
    """T:Devanney's Goat
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Miss McLeod's",
    "reel",
    "G",
    """T:Miss McLeod's
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "GeenFields of Rossbeigh",
    "reel",
    None,
    """T:GeenFields of Rossbeigh
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Congress Reel",
    "reel",
    None,
    """T:Congress Reel
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Over the Moor to Maggie",
    "reel",
    None,
    """T:Over the Moor to Maggie
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Trip to Durrow",
    "reel",
    None,
    """T:Trip to Durrow
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Frank's Reel",
    "reel",
    None,
    """T:Frank's Reel
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Thrush in the Straw",
    "jig",
    None,
    """T:Thrush in the Straw
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Lark on the Strand",
    "jig",
    None,
    """T:Lark on the Strand
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Trip to the Cottage",
    "jig",
    None,
    """T:Trip to the Cottage
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Calliope House",
    "jig",
    None,
    """T:Calliope House
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Her Long Golden Hair",
    "hornpipe",
    None,
    """T:Her Long Golden Hair
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Scully Casey's",
    "hornpipe",
    None,
    """T:Scully Casey's
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Peacock's Feather, The",
    "hornpipe",
    None,
    """T:Peacock's Feather, The
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Chief O'Neill's",
    "hornpipe",
    None,
    """T:Chief O'Neill's
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Humours of Tuamgraney",
    "hornpipe",
    None,
    """T:Humours of Tuamgraney
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Walsh's",
    "jig",
    None,
    """T:Walsh's
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Farewell to Whiskey",
    "jig",
    None,
    """T:Farewell to Whiskey
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Lakes of Sligo",
    "jig",
    None,
    """T:Lakes of Sligo
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Where's the Cat",
    "slide",
    None,
    """T:Where's the Cat
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "The Cat's Rambles to the Child's Saucepan",
    "slide",
    None,
    """T:The Cat's Rambles to the Child's Saucepan
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Sonny's Mazurka",
    "mazurka",
    None,
    """T:Sonny's Mazurka
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Irish Mazurka, The",
    "mazurka",
    None,
    """T:Irish Mazurka, The
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Bonaparte Crossing the Alps",
    "march",
    None,
    """T:Bonaparte Crossing the Alps
%%center Need Notes 
""",
    [],
    []
  ),
#------------------------------------------------------
  Tune(
    "Battle of Aughrim",
    "march",
    None,
    """T:Battle of Aughrim
%%center Need Notes 
""",
    [],
    []
  ),
]

tune_list_alphab: list[Tune] = sorted(tune_list, key=lambda x: x.title)
tune_dict: dict[str, Tune] = {tune.title: tune for tune in tune_list}