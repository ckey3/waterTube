def avg1(lst):
    return sum(lst)/len(lst)

def MyAvg(lst):
    #sum
    s=0
    n=0
    for i in lst:

        s=+i
        n=+1 #tells how many are in array
        print(n,i,s)
    return s/n

x = [3,5,22,11,7]


avg = avg1(x)
print("AVG1:", avg)