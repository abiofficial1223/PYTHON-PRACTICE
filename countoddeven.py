numbers=[12,23,5,8,6]
even_count=0
odd_count=0
even=[]
odd=[]
for num in numbers:
    if num%2==0:
        even_count+=1
        even.append(num)
    elif num%2!=0:
        odd_count+=1
        odd.append(num)
print("even numbers:",even_count)
print("odd numbers:",odd_count)
print("even numbers are:",even)
print("odd numbers are:",odd)
