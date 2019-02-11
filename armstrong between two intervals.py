n,k=map(int,raw_input().split())
for i in range(n+1,k):
    tot=0
    q=i
    while i>0:
        t=i%10
        tot=tot+pow(t,3)
        i=i//10
print i
