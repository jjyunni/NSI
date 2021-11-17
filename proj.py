import math

def db(n):
    b=0
    for i in range(int(math.sqrt(n))//2+2):
        if n>0:
            b+=n%2*10**i
            n=n//2
    print(b)
 
def dhd(n):
    hl=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    h=''
    for i in range(int(math.sqrt(n))//16+2):
        if n>0:
            h=hl[n%16]+h
            n=n//16
    print(h)
 
def bd(n, base):
    if base == 2:
        db(n)
    elif base == 16:
        dhd(n)
    else:
        print("choose 2 or 16")
#bd(int(input()),int(input()))
bd(420,16)