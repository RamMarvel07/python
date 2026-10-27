file=open("exe.txt","r")
data=file.read()
file.close()
words=data
freq=data.split()
f={}
for word in freq:
    f[word]=f.get(word,0)+1
print("all words",words)
print("word freq:",freq)
print("most 10",f)