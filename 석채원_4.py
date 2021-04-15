#4번, B835193 석채원

#print result and determine disjoint set
def printGcf(num): 
    print("최대공약수:",num,end="")
    if(num==1):
        print("(서로소 관계입니다)")
    
x = int(input("첫번째 정수:"))
y = int(input("두번째 정수:"))
gcf = 0
# i goes up from 1 to min(x,y)
for i in range(1,min(x,y)+1):
    #if both x,y can be divided by i, i is the gcf
    if(x%i==0)and(y%i==0):
        gcf = i
#pass the greatest gcf as argument of the function
printGcf(gcf)
