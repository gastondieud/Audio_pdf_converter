


caréelambda= lambda x: x * x
delta=lambda x,y:x+2*y+5

nums=[1, 2, 3, 4, 5, 6]
carréemap= map(caréelambda,nums)
for num in carréemap:
    print(num)