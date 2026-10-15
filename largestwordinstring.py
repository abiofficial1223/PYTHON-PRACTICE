text="i am practicing coding"
words=text.split()
largest=words[0]
for word in words:
    if len(word)> len(largest):
        largest=word
print(largest)        
