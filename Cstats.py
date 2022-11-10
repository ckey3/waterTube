#average list funtion
def avg1(lst):
    return sum(lst)/len(lst)

#residual funtion (y_measured - y_modeled)
def residual(lst1, lst2):
    n=len(lst1)
    x=0
    for i in range(n):
        d = lst1[i] - lst2[i]#singal residual. Make it loop throgh and add all residual to get sum of all residuals
        x += d**2
       # print(i, lst1[i], lst2[i],d,x)       prints: how many, list 1, list 2, residual, sum of residual
    return x

# mean difference
def meanDiff(lst1):
    n=len(lst1)
    x=0
    avg = avg1(lst1)
    for i in range(n):
        d = (lst1[i] - avg)**2
        x+=d
    return x



