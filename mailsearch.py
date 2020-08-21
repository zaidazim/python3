fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File not found')
    quit()
count = 0
for line in fh:
    line = line.rstrip()
    wrds = line.split()
    if len(wrds) < 3:
        continue
    if wrds[0] != 'From':
        continue
    count += 1
    print(wrds[1])
print('There were',(count), 'lines in the file with From as the first word')
