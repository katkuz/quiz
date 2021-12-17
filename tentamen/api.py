import requests
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1


def get_nobel_prizes(parameters):
    """Get list of nobel prizes for selected parameters

        parameters
            argument to be send to api to get desires info about prizes
        """
    return requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=parameters).json()
