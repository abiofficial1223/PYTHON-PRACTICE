numbers=[12,23,5,7,3]
smallest=numbers[0]
second_smallest=numbers[0]
for num in numbers:
    if num<smallest:
        second_smallest=smallest
        smallest=num
    
    elif num>smallest and num!=smallest:
        second_smallest=num
print("the smallest number is:",smallest)
print("the second smallest number is:",second_smallest)
