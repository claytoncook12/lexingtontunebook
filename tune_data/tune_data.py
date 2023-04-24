from tune_data.model.tune import Tune, YoutubeVideoEmbed, AudioReferences

tune_list: list[Tune] = [
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
  )
]