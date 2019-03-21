import collections
ship = {"NAME": "Albatross",
         "BLASTERS":13,
         "THRUSTERS":18,
         "HP":50,
         "PRICE":250}

print ship

ship = collections.OrderedDict(ship)

print ship


new_dict = collections.OrderedDict()
print new_dict

new_dict["NAME"]=ship["NAME"]
new_dict["HP"]=ship["HP"]
new_dict["BLASTERS"]=ship["BLASTERS"]
new_dict["PRICE"]=ship["PRICE"]
new_dict["THRUSTERS"]=ship["THRUSTERS"]

print new_dict
