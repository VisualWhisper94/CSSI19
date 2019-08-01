def CharacterCount(word):
    word = raw_input ("Enther a Word:")
    d = {}
for i in word:
    if d.has_key(i):
        d[i]=d[i]+1
    else:
        d[i]=1
for i,j in d.items():
    print x,":",y