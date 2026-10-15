abi=[12,23,25,55,87,90]
largest=abi[0]
second=abi[0]
for number in abi:
    if number>largest:
        second=largest
        largest=number
    elif number>second and number!=largest:
        second=number
print("largest is:",largest)
print("second largest is:",second)
