import numpy as np

#residual numpy way
def residualNumpy(lst1,lst2):
    d = np.array(lst1) - np.array(lst2)
    print(d)
    s=sum(d)
    return s


# conventional
def residual(lst1, lst2):
    n=len(lst1)
    x=0
    for i in range(n):
        d = lst1[i] - lst2[i]#singal residual. Make it loop throgh and add all residual to get sum of all residuals
        x += d
        print(i, lst1[i], lst2[i],d,x)
    return x 



x = [1,7,12,17,22,26]
y = [0,10,20,30,40,50]

#print conventional
r = residual(x,y)
print("sum rediduals:", r)

#print numpy
res = residualNumpy(x,y)
print(f"residual: {res}")