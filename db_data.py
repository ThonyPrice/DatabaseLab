# This data is used to populate the Hospital db via fillDB.py

# Data for patients in Queue;
#   TeamID, Name, Age, Gender, Issue, Priority
queue_data = [
    ['1', 'Adam',   23, 'M', 'Broken neck',     3],
    ['1', 'Berit',  45, 'F', 'Broken arm',      4],
    ['1', 'Carl',   54, 'M', 'Broken back',     2],
    ['1', 'Dan',    4,  'M', 'Broken arm',      1],
    ['2', 'Erik',   77, 'M', 'Snake bite',      4],
    ['2', 'Fiona',  24, 'F', 'Dog bite',        2],
    ['2', 'Gaston', 64, 'M', 'Cat bite',        3],
    ['2', 'Hans',   59, 'M', 'Cat bite',        5],
    ['2', 'Iris',   71, 'F', 'Dog bite',        4],
    ['3', 'Juan',   8,  'M', 'Chest pain',      1],
    ['3', 'Kitty',  33, 'F', 'Back pain',       2],
    ['3', 'Lena',   74, 'F', 'Foot pain',       2],
    ['3', 'Max',    28, 'M', 'Back pain',       5],
    ['4', 'Nora',   15, 'F', 'Food allergy',    3],
    ['4', 'Oden',   55, 'M', 'Flower allergy',  5],
    ['4', 'Pat',    82, 'M', 'Sun allergy',     4],
    ['4', 'Rick',   28, 'M', 'Sun allergy',     3],
    ['5', 'Siri',   51, 'F', 'Impact trauma',   2],
    ['5', 'Tage',   40, 'M', 'Serious trauma',  4],
    ['5', 'Ulf',    80, 'M', 'Fake trauma',     3],
    ['5', 'Vera',   66, 'F', 'Impact trauma',   2]
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
    ['Broken neck', 'Plaster'],
    ['Broken neck', 'Neck collar'],
    ['Broken neck', 'Rest'],
    ['Broken arm',  'Rehab'],
    ['Broken arm',  'Arm surgery'],
    ['Broken arm',  'Patience'],
    ['Broken back', 'Crutches'],
    ['Broken back', 'Serious surgery'],
    ['Broken back', 'Back surgery'],
    ['Chest pain',  'Iron lung'],
    ['Chest pain',  'Chest massage'],
    ['Chest pain',  'Chest surgery'],
    ['Back pain',   'Back massage'],
    ['Back pain',   'Chriropracticy'],
    ['Back pain',   'Acupuncture'],
    ['Sun allergy', 'Shade tratment'],
    ['Sun allergy', 'Sun surgery'],
    ['Sun allergy', 'Sun vaccination'],
    ['Snake bite', 'Snake vaccine'],
    ['Snake bite',  'Snake surgery'],
    ['Snake bite',  'Poison antidote'],
    ['Dog bite',    'Amputation'],
    ['Dog bite',    'Serious amputation'],
    ['Dog bite',    'Catnip'],
    ['Fake trauma', 'Trauma surgery'],
    ['Fake trauma', 'Fake surgery'],
    ['Fake trauma', 'Trauma treatment'],
    ['Serious trauma', 'Surgery1'],
    ['Serious trauma', 'Surgery2'],
    ['Serious trauma', 'Surgery3']
]

