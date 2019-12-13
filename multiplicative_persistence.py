def mul(n):
    ans = 1
    while(n != 0):
        ans *= n%10
        n = n//10
    return ans

def mult_per(n):
    count = 0
    ans = n
    while(ans >= 10):
        ans = mul(ans)
        #print(ans)
        count += 1
    return count


counter = 0
record = -1
while True:
    per = mult_per(counter)
    if(per > record):
        print(counter,per)
        record += 1
    counter += 1


