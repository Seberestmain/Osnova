array = ["Hello", "2", "world", ":-)"]
finisharray = []
for i in array:
    if len(i) <= 3:
        finisharray.append(i)
print(finisharray)