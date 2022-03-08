def isPossible(x, y,a,b, k):
    minMoves = abs(x-a) + abs(y-b)
    if (k >= minMoves and (k - minMoves) % 2 == 0):
        return True
    return False
 
for _ in range(int(input())):
    a,b,c,d,k=map(int,input().split())
    if isPossible(a,b,c,d,k):
        print("YES")
    else:
        print("NO")
