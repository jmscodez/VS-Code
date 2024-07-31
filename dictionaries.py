#dictionaries --> ep7
band = {
    "vocals":"Plant",
    "guitar":"Page"
}

band2 = dict(vocals="Plant",guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

#Access items
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values

print(band.values())

#list values/keys as Tuples
print(band.items())

#verify if value exists
print("guitar" in band)
print("triangle" in band)

#change values
band["vocals"] = "coverdale"
band.update({"bass": f"JPJ"})

print(band)

#Remove items
print(band.pop("bass"))

#add items
band["drums"] = "Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

#delete and clear
band["drums"] = "Bonham"
del band ["drums"]
print(band)

band2.clear()






#SETS

nums = {1, 2, 3, 4}
nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no duplicates allowed
nums3 = {4, 6, 3, 2}

print(nums3)

#true is a dupe of 1, False is a dupe of 0


new = {1, 2, 3, 4, 8, False}
print(new)

morenums = {5,6,7}

new.update(morenums)

print(new) 


#merge 2 sets into 1
one = {1,2,3}
two = {5,6,7}

merged = one.union(two)
print(merged)


#keep only duplicates 
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

#keep all but duplicates 
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
