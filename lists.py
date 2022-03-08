N = int(input())
l=[]
for i in range(N):
    comm=input().split()
    if comm[0]=="insert":
        l.insert(int(comm[1]),int(comm[2]))
    elif comm[0]=="remove":
        l.remove(int(comm[1]))
    elif comm[0]=="append":
        l.append(int(comm[1]))
    elif comm[0]=="print":
        print(l)
    elif comm[0]=="sort":
        l.sort()
    elif comm[0]=="reverse":
        l.reverse()
    elif comm[0]=="pop" and l!=[]:
        l.pop()
