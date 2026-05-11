import requests
import os
import json
from urllib.parse import quote

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

frazy = [
    "aaawaria",
    "alcomindz",
    "alcmdz",
    "belmondo",
    "belmondawg",
    "hehe",
    "poppyn",
    "benito",
    "diho",
    "gmll",
    "gm2l",
    "don poldon",
    "gicik amane",
    "amen pacierzu",
    "gsp",
    "hewra",
    "kaz bałagane",
    "narkopop",
    "koldi",
    "malik montana",
    "mlody dron",
    "mobbyn",
    "uhqqow",
    "og olgierd",
    "gooch gang",
    "olosolo",
    "oyche doniz",
    "ricci",
    "rogal ddl",
    "sentino",
    "sicarios",
    "tax free",
    "tuzza",
    "tuzza globale"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    with open("seen.json", "r") as f:
        seen = json.load(f)
except:
    seen = []

for fraza in frazy:

    url = f"https://www.vinted.pl/api/v2/catalog/items?search_text={quote(fraza)}"

    response = requests.get(url, headers=headers)

    try:
        data = response.json()
    except:
        continue

    items = data.get("items", [])

    for item in items[:5]:

        item_id = str(item.get("id"))

        if item_id in seen:
            continue

        title = item.get("title", "Brak tytułu")
        price = item.get("price", "Brak ceny")

        item_id_for_link = item.get("id")
        link = f"https://www.vinted.pl/items/{item_id_for_link}"

        title_lower = title.lower()

        top_keywords = [
            "hoodie",
            "bluza",
            "t-shirt",
            "tshirt",
            "koszulka",
            "crewneck",
            "longsleeve",
            "koszula",
            "zip",
            "sweatshirt"
        ]

        blocked_keywords = [
            "spodnie",
            "pants",
            "jeans",
            "buty",
            "shoes",
            "czapka",
            "cap",
            "torba",
            "bag"
        ]

        if not any(word in title_lower for word in top_keywords):
            continue

        if any(word in title_lower for word in blocked_keywords):
            continue

        text = f"""
NOWA OFERTA

FRAZA: {fraza}

{title}
Cena: {price}

{link}
"""

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": text
            }
        )

        seen.append(item_id)

with open("seen.json", "w") as f:
    json.dump(seen, f)
