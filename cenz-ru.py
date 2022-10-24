import json
from fuzzywuzzy import fuzz

msg = ""
bad_words = json.load(open("cenz-ru.json"))

for i in msg.text.split(" "):
    for b in bad_words:
        if  fuzz.ratio(i.lower(), b) >= 60:
            print("Найден мат в строке")
