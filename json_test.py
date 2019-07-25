import json

with open('148.json') as artfile:
    art = json.load(artfile)
    print(art['description'])

#loads and dumps
nums = json.loads("[1, 2, 3]") #load a string into a python object
print(json.dumps(nums)) #turn a python object into a string