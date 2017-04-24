# This data is used to populate the Hospital db via fillDB.py

# Data for patients in Queue;
#   PersonID, TeamID, Name, Age, Gender, Issue, Priority
queue_data = [
    ['19910220-4899',   1, 'Adam',   23, 'M', 'Broken neck',     3,  '13:00'],
    ['19890313-1300',   1, 'Berit',  45, 'F', 'Broken arm',      4,  '14:00'],
    ['19450211-1400',   1, 'Carl',   54, 'M', 'Broken back',     2,  '13:45'],
    ['19930413-1121',   1, 'Dan',    4,  'M', 'Broken arm',      1,  '15:00'],
    ['19930413-1156',   2, 'Erik',   77, 'M', 'Snake bite',      4,  '14:45'],
    ['19930413-1460',   2, 'Fiona',  24, 'F', 'Dog bite',        2,  '15:15'],
    ['19930413-6330',   2, 'Gaston', 64, 'M', 'Snake bite',      3,  '14:30'],
    ['19930413-5530',   2, 'Hans',   59, 'M', 'Snake bite',      5,  '13:00'],
    ['19960402-2430',   2, 'Iris',   71, 'F', 'Dog bite',        4,  '13:56'],
    ['19971231-1145',   3, 'Juan',   8,  'M', 'Chest pain',      1,  '15:22'],
    ['19971213-1300',   3, 'Kitty',  33, 'F', 'Back pain',       2,  '13:11'],
    ['19971216-1145',   3, 'Lena',   74, 'F', 'Foot pain',       2,  '14:47'],
    ['19971202-1350',   3, 'Max',    28, 'M', 'Back pain',       5,  '13:30'],
    ['19971201-1350',   4, 'Nora',   15, 'F', 'Food allergy',    3,  '13:37'],
    ['19971211-1240',   4, 'Oden',   55, 'M', 'Sun allergy',     5,  '14:12'],
    ['19971215-1550',   4, 'Pat',    82, 'M', 'Sun allergy',     4,  '11:06'],
    ['19970636-1230',   4, 'Rick',   28, 'M', 'Sun allergy',     3,  '12:12'],
    ['19970536-7650',   5, 'Siri',   51, 'F', 'Impact trauma',   2,  '14:59'],
    ['19971436-1345',   5, 'Tage',   40, 'M', 'Serious trauma',  4,  '13:13'],
    ['19971036-1624',   5, 'Ulf',    80, 'M', 'Fake trauma',     3,  '12:48'],
    ['19971125-8245',   5, 'Vera',   66, 'F', 'Impact trauma',   2,  '13:55']
]

# Data for Teams;
#   TeamID, Head of team, Issue1, Issue2, Issue3
team_data = [
    [1, 'Name1', 'Broken neck', 'Broken arm', 'Broken back'],
    [2, 'Name2', 'Snake bite', 'Back pain', 'Chest pain'],
    [3, 'Name3', 'Snake bite', 'Dog bite', 'Broken arm'],
    [4, 'Name4', 'Fake trauma', 'Serious trauma', 'Sun allergy'],
    [5, 'Name5', 'Snake bite', 'Chest pain', 'Broken neck']
]

# Data for Treatments;
#   Issue, Treatment
issues_and_treatments = [
    ['Broken neck', 'Plaster',      100],
    ['Broken neck', 'Neck collar',  150],
    ['Broken neck', 'Rest',         50],
    ['Broken arm',  'Rehab',        250],
    ['Broken arm',  'Arm surgery',  500],
    ['Broken arm',  'Patience',     20],
    ['Broken back', 'Crutches',     180],
    ['Broken back', 'Serious surgery', 850],
    ['Broken back', 'Back surgery', 700],
    ['Chest pain',  'Iron lung',    450],
    ['Chest pain',  'Chest massage',    300],
    ['Chest pain',  'Chest surgery',    350],
    ['Back pain',   'Back massage',     600],
    ['Back pain',   'Chriropracticy',   550],
    ['Back pain',   'Acupuncture',      550],
    ['Sun allergy', 'Shade tratment',   380],
    ['Sun allergy', 'Sun surgery',      130],
    ['Sun allergy', 'Sun vaccination',  390],
    ['Snake bite', 'Snake vaccine',     260],
    ['Snake bite',  'Snake surgery',    700],
    ['Snake bite',  'Poison antidote',  800],
    ['Dog bite',    'Amputation',       990],
    ['Dog bite',    'Serious amputation',   120],
    ['Dog bite',    'Catnip',           50],
    ['Fake trauma', 'Trauma surgery',   890],
    ['Fake trauma', 'Fake surgery',     1000],
    ['Fake trauma', 'Trauma treatment',     280],
    ['Serious trauma', 'Surgery1',      600],
    ['Serious trauma', 'Surgery2',      600],
    ['Serious trauma', 'Surgery3',      600]
]

drugs_data = [
    ['Blue pill',   45],
    ['Red pill',    20],
    ['Cyan pill',   75],
    ['Orange pill', 15],
    ['Green pill',  30],
    ['Black pill',  50],
    ['White pill',  45],
    ['Grey pill',   25],
    ['Violet pill', 60],
    ['Two pills',   95],
]
