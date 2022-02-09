arr = [2,6,8,14]
answer = []
gcd = sorted(arr,reverse = True)
lcm = gcd[0]
for i in range(1,len(gcd)):
    lcm *= gcd[i]
    while gcd[i] !=0:
        temp1 = gcd[i-1]
        gcd[i-1] = gcd[i]
        gcd[i] = temp1%gcd[i]
    gcd[i] = lcm/gcd[i-1]
    lcm = gcd[i]
    

temp = 0 