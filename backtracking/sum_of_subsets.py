import numpy as np

m=35
w=[15,7,20,5,18,10,12]
sum=np.sum(w)
# print(w)
n=len(w)
x=np.zeros(n)
x=x.astype(np.int)
def sum_of_subsets(s,k,r):
    # print(s)
    x[k]=1
    if s+w[k] == m:
        for j in range(k+1,n):
            x[j]=0
        print(x)
    else:
        if (s+w[k]+w[k+1])<= m:
            sum_of_subsets(s+w[k],k+1,r-w[k])
    if((s+r-w[k])>=m) and ((s+w[k+1])<=m):
        x[k]=0
        sum_of_subsets(s,k+1,r-w[k])
print("Possible solutions are: ")
sum_of_subsets(0,0,sum)
