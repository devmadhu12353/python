s1={'1001','1009','1008','1007','1005','1003'}
s2={'1001','1002','1006','1007','1003'}

print("visitor on both days:",s1&s2)
print("visitor on one of the days:",s1^s2)
print("total unique visitor on both days:",s1|s2)
print("visited on first date also visited on second day:",s1 in s2)
