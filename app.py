import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead,Enter Y or N \n" % get_close_matches(w,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'N':
            return "Word does not exit"
    else:
        return "The word doesn't exist"



word = input ("Enter word :")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
