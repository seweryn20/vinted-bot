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

for fraza in frazy:

    url = f"https://www.vinted.pl/catalog?search_text={quote(fraza)}"

    text = f"""
NOWA FRAZA

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
