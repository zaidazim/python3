hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
if(h > 40):
    rp = h * r
    otp = (h - 40) * (0.5 * r)
    tp = rp + otp
else:
    tp = h * r
print(tp)
