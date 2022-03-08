


cost=int(input())
year=int(input())
rate=int(input())
if rate%5>0:
    print("Invalid input")
elif rate<5 or rate>100:
    print("Invalid input")
else:
    while year!=1:
        cost=cost-rate*cost/100



        year-=1
    print(round(cost))
