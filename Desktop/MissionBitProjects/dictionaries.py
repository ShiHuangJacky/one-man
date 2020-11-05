names = ["tyler", "jacky", "ryan", "ramiro", "kingsley"]

names_and_heights = {"tyler": {"feet": 5}, "inches": 11, 
"jacky": {"feet": 6, "inches": 5}, 
"ryan": {"feet":3, "inches": 11}}

print(str(names_and_heights["tyler"]["feet"]) + "' " + str
(names_and_heights["tyler"]["inches"]) 

        # key       #value
# key-value pairs

# updating an existing key
names_and_heights["ryan"]["feet"] = 7

# adding a new key-value pair
names_and_heights["ramiro"]["feet"] = 5

names_and_heights["ramiro"] = {feet: 5, "inches": 3}

names_and_heights.update({
    "angelo": {"feet":0, "inches": 0}, 
    "allistair": {"feet": 0, "inches": 0}
    })
print(names_and_heights)

for key in names_and_heights:
    print(key)

for value in names_and_heights.values():
    print(value)