# sets = collection which is unordered, unindexed. No duplicate values 

# utensils = {"spoon","fork","knife"}
# dishes = {"bowl","plate","cup","knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
dinner_table = utensils.union(dishes)

# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))

for x in dinner_table:
    print(x)


# utensils = {"plate","spoon","knife"}

# for x in utensils:
#     print(x)