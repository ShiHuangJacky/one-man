# names = [["jenny", 61], ["alexus", 70] ["sam", 67] ["grace", 64]]

# names = [["jenny", 67], ["alexus", 70]]

# print(names[1][1])
# print(names[0][0] + " " + str(names[0][1]) + " inches tall")

# names = ["Jenny", "Alexus"]
# heights = [61, 70]

# names_and_heights = zip(names,heights)

# print(list(names_and_heights))

# tuples: (x, y) and cannot be changed
# list: [x, y]

# print(names_and_heights[0][0])

names = ["jenny", "alexus"]
print("Before adding \"sam\": ", names)
names.append("sam")
print("After adding \"sam\": ", names)

# names.insert(0, "alex")

# range(x)
#start: 0
#stop: x
#step: 1


#range(x, y, z)
#start: x
#stop: y-1
#step:z

new_range = list(range(10))
print(new_range)

even_range = list(range(0,21,2))
print(even_range)