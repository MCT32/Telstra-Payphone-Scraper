import requests
import json


PAGE = 0
POINT = {
    "lat":-37.7353584,
    "lon":144.6707088
}
MAX_RADIUS = 516577
STATE = "VIC"


URL = "https://tapi.telstra.com/presentation/v1/tcom/geo/payphones/list"
METHOD = "POST"
HEADERS = {
    "Content-Type": "application/json",
    "source": "tcom"
}

done = False

output = []

# Loop pages
while not done:
    BODY = {
        "point": POINT,
        "radius":10000,
        "pagination": {
            "size":100,
            "from":PAGE * 100
        }
    }
    
    data = requests.request(METHOD, URL, headers=HEADERS, json=BODY).json()

    phones = data["results"][0]["value"][0]["featureList"]

    for phone in phones:
        if phone["distance"] > MAX_RADIUS:
            done = True
            break

        if phone["state"] == STATE:
            output.append({
                "latitude": phone["latitude"],
                "longitude": phone["longitude"],
                "address": phone["address"],
                "state": phone["state"],
                "postcode": phone["postcode"],
                "phone_attributes": phone["phone_attributes"],
                "fnn": phone["fnn"],
            })
    
    PAGE = PAGE + 1

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
