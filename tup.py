fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File not found')
    quit()

list = []
dic = dict()

for line in fh:
    line = line.rstrip()
    wrds = line.split()
    if len(wrds) < 3:
        continue
    if wrds[0] != 'From':
        continue
    time = (wrds[5])            #extracting time from the line and storing it in a variable
    time = time.split(':')
    hour = time[0]              #extracting the hour part from the time variable
    list.append(hour)           #storing all the hour variables in a list

for item in list:
    dic[item] = dic.get(item, 0) + 1    #making a dictionary of hour and counter variable
for key, val in sorted(dic.items()):
    print(key, val)
