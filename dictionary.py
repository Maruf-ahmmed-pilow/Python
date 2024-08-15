capitals = {"USA":"Washington DC",
            "INDIA":"New Dellhi",
            "BANGLADESH":"Dhaka",
            "SRILANGKA":"Colombo",
            "PAKISTAN":"Islamabad",
            }
capitals.update({"Germany": "Berlin"})
capitals.pop("SRILANGKA")
#capitals.clear()
print(capitals)
print(capitals.get('GERMANY'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key,":",value)