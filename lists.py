fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File not found')
    quit()
new = []
for line in fh:
    line = line.split()
    for word in line:
        str = word
        if str not in new:
            new.append(word)
new.sort()
print(new)
