def kadane(l):
    temp=0
    nc=0
    res=0
    for i in range(len(l)):
        if l[i]<0:
            nc+=1
        temp+=l[i]
        if temp<0:
            temp=0
        res=max(res,temp)
    return res
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        res=[]
        for i in range(len(B)):
            if B[i][0]==1:
                temp=A.index(B[i][1])
                A[temp]=B[i][2]
            else:
                odd=0
                left=B[i][1]-1
                right=B[i][2]-1
                temp=A[left:right+1]
                for i in range(left,right):
                    if odd==1:
                        temp[i]=temp[i]*-1
                        odd=0
                    else:
                        odd=1
                res.append(kadane(temp[left:right+1]))
        return res
