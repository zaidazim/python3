fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File not found')
    quit()
senderid = []
mail = dict()
for line in fh:
    line = line.rstrip()
    wrds = line.split()
    if len(wrds) < 3:
        continue
    if wrds[0] != 'From':
        continue
    senderid.append(wrds[1])
for ids in senderid:
    mail[ids] = mail.get(ids, 0) + 1
maxid = None
maxcount = None
for id, count in mail.items():
    if maxcount is None or count > maxcount:
        maxid = id
        maxcount = count
print(maxid, maxcount)
