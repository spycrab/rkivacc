from rkivacc.report import RKIReport

URL = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquotenmonitoring.xlsx?__blob=publicationFile"

WORKSHEET_INDEX = 1
TABLE_FIRST_ROW = 2
TABLE_LENGTH = 16

# Pulled out of by reversing the per capita stats via the total vaccination numbers
POPULATION_STATS = {
    "Baden-Württemberg": 11100394,
    "Bayern": 13124737,
    "Berlin": 3669491,
    "Brandenburg": 2521893,
    "Bremen": 681202,
    "Hamburg": 1847253,
    "Hessen": 6288080,
    "Mecklenburg-Vorpommern": 1608138,
    "Niedersachsen": 7993608,
    "Nordrhein-Westfalen": 17947221,
    "Rheinland-Pfalz": 4093903,
    "Saarland": 986887,
    "Sachsen": 4071971,
    "Sachsen-Anhalt": 2194782,
    "Schleswig-Holstein": 2903773,
    "Thüringen": 2133378,
    "total": 83166711
}
