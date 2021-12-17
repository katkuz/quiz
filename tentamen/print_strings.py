from datetime import date
from tentamen.category import cat


WRONG_YEAR_MESSAGE = "Fel år. Ska vara mellan 1901 och " + str(date.today().year) + ". Prova igen"
QUITING_MESSAGE = "quiting..."
WRONG_CATEGORY_MESSAGE = "Fel kategori. Prova igen"
WRONG_INPUT_MESSAGE = "Fel input. Prova igen"
START_MESSAGE = """
Ange ett år och fält
Exempelvis 1965 fysik

Ni kan avsluta programmet med att skriva Q

Möjliga kategorier är:
"""
for key, value in cat.items():
    START_MESSAGE = START_MESSAGE + "  " + key + "\n"
