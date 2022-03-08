for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    l = list(map(int, input().split()))
    s=list(s)
    curr = 0
    for x, y in zip(l, l[1:]):
        curr += 2 if x == y else 1
        l = ["_"] + l + ["_"]
    for i in l:
        temp = 2 if l[i] == l[i+1] else 1
        temp += 2 if l[i] == l[i-1] else 1
        if l[q] == "0":
            l[q] = "1"
        else:
            l[q] = "0"
        temp2 = 2 if l[i] == l[i+1] else 1
        temp2 += 2 if l[i] == l[i-1] else 1
        curr += (temp - temp2)
        print(curr)
