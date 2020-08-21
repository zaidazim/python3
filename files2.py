fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File not found')
    quit()
add = 0.0
count = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count += 1
        spos = line.find('0')
        strnum = line[spos:]
        fvalue = float(strnum)
        add += fvalue
avgspam = add/count
print('Average spam confidence:',(avgspam))
