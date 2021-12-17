import requests
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1


def get_nobel_prizes(c):
    return requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=c).json()
