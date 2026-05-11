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
    "poppyn",
    "benito",
    "diho",
    "gmll",
    "gm2l",
    "don poldon",
    "gicik amane",
    "gsp",
    "hewra",
    "kaz bałagane",
    "koldi",
    "malik montana",
    "mlody dron",
    "mobbyn",
    "og olgierd",
    "olosolo",
    "oyche doniz",
    "ricci",
    "rogal ddl",
    "sentino",
    "sicarios",
    "tax free",
    "tuzza"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

for fraza in frazy:

    url = f"https://www.vinted.pl/catalog?search_text={quote(fraza)}"

    response = requests.get(url, headers=headers)

    text = f"""
NOWA FRAZA SPRAWDZONA

{fraza}

LINK:
{url}
"""

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

    time.sleep(2)
