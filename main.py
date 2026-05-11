import requests
import os
import json
import re
from urllib.parse import quote
from bs4 import BeautifulSoup

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

ALLOWED_SIZES = ["M", "L", "XL"]

TOP_KEYWORDS = [
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

BLOCKED_KEYWORDS = [
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

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    with open("seen.json", "r") as f:
        seen = json.load(f)
except:
    seen = []

for fraza in frazy:

    url = f"https://www.vinted.pl/catalog?search_text={quote(fraza)}"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)

    for link in links:

        href = link["href"]

        if "/items/" not in href:
            continue

        item_id_match = re.search(r'/items/(\d+)', href)

        if not item_id_match:
            continue

        item_id = item_id_match.group(1)

        if item_id in seen:
            continue

        text_content = link.get_text(" ", strip=True).lower()

        if not any(word in text_content for word in TOP_KEYWORDS):
            continue

        if any(word in text_content for word in BLOCKED_KEYWORDS):
            continue

        size_ok = any(size.lower() in text_content for size in ["m", "l", "xl"])

        if not size_ok:
            continue

        full_link = f"https://www.vinted.pl{href}"

        message = f"""
NOWA OFERTA

FRAZA: {fraza}

{full_link}
"""

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": message
            }
        )

        seen.append(item_id)

with open("seen.json", "w") as f:
    json.dump(seen, f)
