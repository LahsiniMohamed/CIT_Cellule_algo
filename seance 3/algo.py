"""
0(1)  ---------> print - affectation - if ........

0(logn)

0(n)  ---------> selection --- for()

0(nlogn)


0(n**2)--------> manipulation des matrices


"""
tab = [5,2,4,89,4,3,7,5,4,9,2,6,7,1]
n = len(tab)
for i in range(n):
    for j in range(0, n-i-1):
        if tab[j] > tab[j+1] :
            tab[j], tab[j+1] = tab[j+1], tab[j]
        #### 0(1)
    #0(n-i-1)
#0(n**2)    


##### best case : 0(n)

print(tab)


