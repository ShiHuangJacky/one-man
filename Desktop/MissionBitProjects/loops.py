# names = ["alex", "allistair", "andrew", "angelo", "elijah", "george", "jonathan"]
# for p in names:
#     print(p)

# rng = list(range(6))
# print(rng)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
for num in lst:
    print(num*2)
print(lst)

for p in range(len(lst)):
    lst[p] = 2 * lst[p]
    print(lst[p])

print(lst)