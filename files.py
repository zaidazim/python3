fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File not found')
    quit()
for line in fh:
    x = line.rstrip()
    print(x.upper())
