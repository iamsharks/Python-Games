s=input().split()
min_word=s[0]
min_length=len(min_word)
for word in s[1:]:
    if len(word)<min_length:
        min_word=word
        min_length=len(word)
print(min_word)

   