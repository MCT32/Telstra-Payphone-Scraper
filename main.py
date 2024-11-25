import requests


PAGE = 0
POINT = {
    "lat":-37.7353584,
    "lon":144.6707088
}
# MAX_RADIUS = 0


URL = "https://tapi.telstra.com/presentation/v1/tcom/geo/payphones/list"
METHOD = "POST"
HEADERS = {
    "Content-Type": "application/json",
    "source": "tcom"
}
BODY = {
    "point": POINT,
    "radius":10000,
    "pagination": {
        "size":100,
        "from":PAGE * 100
    }
}

data = requests.request(METHOD, URL, headers=HEADERS, json=BODY).json()

print(data)
