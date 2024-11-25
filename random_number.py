import json
import random
import os


with open('output.json', 'r', encoding='utf-8') as f:
    phones = json.load(f)

    while True:
        phone = random.choice(phones)

        os.system('cls')
        print(f"Address: {phone["address"]}\nPhone: {phone["fnn"]}\nMap: http://www.openstreetmap.org/?mlat={phone["latitude"]}&mlon={phone["longitude"]}&zoom=12")

        input()
