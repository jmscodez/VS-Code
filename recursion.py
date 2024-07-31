def add_one (num):
    if(num>=9):
        return num+1
    total = num + 1
    print (total)

    return add_one(total)

# will only count until 9 unless you call another function as seen below

NewTotal = add_one(0) 
print(NewTotal)