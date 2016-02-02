def machtv2(a,n):
    if n == 0:
        return 1
    if n < 0:
        return 1/machtv2(a,-n);
    m = 1
    for dummy in range(0,n): # dummy,unused,_ : Python kent geen n.times
        m = m*a;
    return m

print("2 ^ 8: ", machtv2(2,8))
