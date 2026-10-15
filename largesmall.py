numbers=[12,23,5,7,16]
largest=numbers[0]
smallest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
    elif num==min(numbers):
        smallest=num
print("the largest number is:",largest)
print("the smallest number is:",smallest)
