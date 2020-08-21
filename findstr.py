text = "X-DSPAM-Confidence:    0.8475";
atpos = text.find('0')
spos  = text.find('5')
slicedstr = text[atpos:spos+1]
print(float(slicedstr))
