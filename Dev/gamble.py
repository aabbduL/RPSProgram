import json

def cP():
    with open("data.json", "r") as f:
        data = json.load(f)
        p = data['chip'][0]['player']
    return p

def cC():
    with open("data.json", "r") as f:
        data = json.load(f)
        c = data['chip'][1]['computer']
    return c

def win(a,b):
    with open("data.json", "r") as f:
        data = json.load(f)
    with open("data.json", "w") as f:
        data['chip'][0]['player'] += (a+b)
        data['chip'][1]['computer'] -= (a+b)
        json.dump(data, f, indent=4)
        # print("sukses")

def lose(x,y):
    with open("data.json", "r") as f:
        data = json.load(f)
    with open("data.json", "w") as f:
        data['chip'][0]['player'] -= (x+y)
        data['chip'][1]['computer'] += (x+y)
        json.dump(data, f, indent=4)
        # print("sukses")
